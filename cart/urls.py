
from django.urls import path

from cart.views import cart_view, remove_from_cart, add_to_cart

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('remove_cart/<int:product_id>/', remove_from_cart, name='remove_cart'),
    path('add_cart/<int:product_id>/', add_to_cart, name='add_cart'),

]
