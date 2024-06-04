from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.contrib import messages

from cart.models import CartItem, Cart
from cart.views import cart_view
from monapp.views import connexion
from .models import Product
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


def category(request):
    
    return render(request, 'category.html' )  


def boutique(request):
    # Récupérer les produits en promotion et ceux qui ne le sont pas
    promo = Product.objects.filter(promo=True)
    object_list = Product.objects.filter(promo=False)
    object = Product.objects.all()

    # Pagination des produits non promos
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)  # Utilisation de paginator.get_page pour récupérer les produits paginés

    return render(request, 'boutique.html',
                  {'promo': promo, 'object_list': products,'object':object})  # Passer les produits paginés à la template


def productlistview(request):
    # Récupérer les produits en promotion et ceux qui ne le sont pas
    promo = Product.objects.filter(promo=True)
    object_list = Product.objects.filter(promo=False)

    # Pagination des produits non promos
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)  # Utilisation de paginator.get_page pour récupérer les produits paginés

    return render(request, 'accueil.html',
                  {'promo': promo, 'object_list': products})  # Passer les produits paginés à la template


def produitdetailview(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        # Récupérer ou créer le panier de l'utilisateur et l'élément de panier pour le produit
        user_cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, _ = CartItem.objects.get_or_create(cart=user_cart, product=product)

        if cart_item is not None:  # Vérifier si l'élément de panier a été correctement récupéré ou créé
            cart_item.quantity += quantity
            cart_item.save()
            messages.success(request,
                             f"{quantity} {product.name} successfully added!")  # Message de succès entre guillemets

        return HttpResponseRedirect('../../cart')

    other_product = Product.objects.filter(category=product.category).exclude(pk=product_id)[:3]

    return render(request, 'detail.html', {'product': product, 'other_product': other_product})
