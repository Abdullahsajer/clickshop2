from django.urls import path
from . import views

app_name = 'sales'
urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]
