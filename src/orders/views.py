from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created

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
