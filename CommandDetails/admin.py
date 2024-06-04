from django.contrib import admin

from CommandDetails.models import CommandDetail


# Register your models here.

class CommandDetailAdmin(admin.ModelAdmin):
    list_display = ['command', 'products', 'price', 'quantity']
    search_fields = ['quantity', 'price', 'command', 'products', ]
    list_filter = ['quantity', 'price', 'command', 'products']


admin.site.register(CommandDetail, CommandDetailAdmin)
