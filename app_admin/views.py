from urllib import request

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from category.forms import CategoryForm
from category.models import Category
from products.forms import ProductsForm
from products.models import Product


# Create your views here.
# @permission_required('has_permission', raise_exception=True)
@login_required(login_url='connexion')
def my_articles(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'my_articles.html', {'products': products})


# @permission_required('has_permission',raise_exception=True)
@login_required(login_url='connexion',redirect_field_name='dashboard')
def dashboard(request):
    return render(request, 'dashboard.html')


# PermissionRequiredMixin,
class ListProductView(LoginRequiredMixin, ListView):
    queryset = Product.objects.all()
    permission_required = 'has_permission'
    raise_exception = True
    template_name = "manager.html"


# PermissionRequiredMixin,
class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    permission_required = 'has_permission'
    raise_exception = True
    form_class = CategoryForm
    template_name = "create.html"
    success_url = "createview"


# PermissionRequiredMixin,
class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductsForm
    permission_required = 'has_permission'
    raise_exception = True
    template_name = "create.html"
    success_url = "../manager"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# PermissionRequiredMixin,
class UpdateProductView(LoginRequiredMixin, UpdateView):
    queryset = Product.objects.all()
    template_name = "create.html"
    permission_required = 'has_permission'
    raise_exception = True
    model = Product
    form_class = ProductsForm


# PermissionRequiredMixin,
class DeleteProductView(LoginRequiredMixin, DeleteView):
    queryset = Product.objects.all()
    template_name = "delete.html"
    permission_required = 'has_permission'
    raise_exception = True
    model = Product
    success_url = '../../manager'
