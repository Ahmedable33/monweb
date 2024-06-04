from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product


# Create your views here.
#
# def pagination(request):
#     object_list = Product.objects.all()
#     paginator = Paginator(object_list, 2)
#     page = request.GET.get('page')
#     products = paginator.get_page(page)
#     try:
#         object_list = paginator.page(page)
#
#     except PageNotAnInteger:
#         object_list = paginator.page(1)
#
#     except EmptyPage:
#         object_list = paginator.page(paginator)
#
#     return render(request, 'accueil.html', {'object_list': object_list})
