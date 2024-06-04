
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem


@login_required(login_url='connexion')
def cart_view(request):
    user_cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    total = sum(item.quantity * item.product.price for item in cart_items)
    for item in cart_items:
        item.total_price = item.quantity * item.product.price

    return render(request, 'cart.html',
                  {'cart_items': cart_items, 'total': total, 'item.total_price': item.total_price})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def remove_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user_cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=user_cart, product=product)
    quantity = int(request.POST.get('quantity', 1))
    if cart_item.quantity > 1:
        cart_item.quantity -= quantity
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')
