from django.contrib import admin

from command.models import Command


# Register your models here.

class CommandAdmin(admin.ModelAdmin):
    list_display = ['name','email','street','phone','country','zip','city']


admin.site.register(Command, CommandAdmin)
