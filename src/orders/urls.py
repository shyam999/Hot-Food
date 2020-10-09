from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('admin/order/<int:order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf'),
    path('create/', views.order_create, name='order_create'),
]
