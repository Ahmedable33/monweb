from django.template.context_processors import request
from django.urls import path

from .views import  boutique, category, productlistview,produitdetailview

urlpatterns = [

    path("product/", productlistview, name='product'),
    path("", boutique, name='boutique'),
    path("category", category, name='category'),

    path("detail/<int:product_id>/", produitdetailview, name='detail'),

    # path("", Promo.as_view(), name=''),
    # path("p/", promo, name='promo'),
    # path("", pagination, name='page'),
]
