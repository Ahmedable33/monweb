from django.urls import path

from .views import ListProductView, UpdateProductView, CreateProductView, DeleteProductView, CreateCategoryView, \
    dashboard, my_articles

urlpatterns = [

    path("dashboard", dashboard, name='dashboard'),
    path("my_articles", my_articles, name='my_articles'),
    path("manager", ListProductView.as_view(), name='manager'),
    path("createview", CreateProductView.as_view(), name='createview'),
    path("categoryview", CreateCategoryView.as_view(), name='categoryview'),
    path("updateview/<str:slug>/", UpdateProductView.as_view(), name='updateview'),
    path("DeleteProductView/<str:slug>/", DeleteProductView.as_view(), name='deleteview'),

]
