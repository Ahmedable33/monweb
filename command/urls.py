from django.urls import path

from command.views import command, payement

urlpatterns = [

    path("command/", command, name='command'),
    path("payement/", payement, name='payement'),
    # path("detail/", detail, name='detail'),

]
