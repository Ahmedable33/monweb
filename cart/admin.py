from django.contrib import admin

from cart.models import CartItem

from cart.models import Cart


# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']


admin.site.register(CartItem, CartItemAdmin)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ['user', 'get_total_quantity', 'get_total_cost', 'display_products']

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.cartitem_set.all())

    get_total_quantity.short_description = 'Total Quantity'

    def get_total_cost(self, obj):
        return sum(item.product.price * item.quantity for item in obj.cartitem_set.all())

    get_total_cost.short_description = 'Total Cost'

    def display_products(self, obj):
        return ", ".join([item.product.name for item in obj.cartitem_set.all()])

    display_products.short_description = 'Products'


admin.site.register(Cart, CartAdmin)
