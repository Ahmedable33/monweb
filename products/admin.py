from django.contrib import admin

from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'publish']
    search_fields = ['name', 'publish']
    list_filter = ['name', 'price', 'stock', 'publish']


admin.site.register(Product, ProductAdmin)
