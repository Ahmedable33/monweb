from django.views.generic import ListView

from django.shortcuts import render

from .models import Category


# Create your views here.

class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'category.html'
