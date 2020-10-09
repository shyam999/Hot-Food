from django.shortcuts import render,get_object_or_404
from cart.cart import Cart
from .models import OrderItem,Order
from .forms import OrderCreateForm
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            cart.clear()
            order_created.delay(order.id)
            return render(request, 'order/ordered.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/order.html', {'cart': cart, 'form': form})

@staff_member_required
def admin_order_pdf(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    html=render_to_string('order/pdf.html',{'order':order})
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']=f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(BASE_DIR + '/static/css/pdf.css')])
    return response
