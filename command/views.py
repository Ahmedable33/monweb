from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from command.models import Command


# from .forms import UtilisateurForm


# Create your views here.
def command(request):
    if request.method == "POST":
        user = request.user
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        street = request.POST['street']
        city = request.POST['city']
        zip = request.POST['zip']
        country = request.POST['country']
        command = Command.objects.get_or_create(user=user, name=name, email=email, phone=phone, street=street,
                                                city=city,
                                                zip=zip, country=country)
        messages.success(request, "Adress succefully register  ")
        return redirect('payement')
    else:
        Command()
    return render(request, "command.html")


def payement(request):
    return render(request,'payement.html')
