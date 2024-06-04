from django.urls import path

from mails.views import MailListView

urlpatterns = [

    path('mail/', MailListView.as_view(), name='mail'),


]
