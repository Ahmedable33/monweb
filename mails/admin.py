from django.contrib import admin

from .models import Email


# Register your models here.
class Email_Admin(admin.ModelAdmin):
    list_display = ['email', 'message', 'destination', 'date_sent']


admin.site.register(Email, Email_Admin)
