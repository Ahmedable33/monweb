from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# from .forms import UtilisateurForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(email=email):
            messages.error(request, "Ce email a deja un compte")
            return redirect('signup')
        if password2 != password1:
            messages.error(request, "Les mots de pass ne correspond pas")
            return redirect('signup')

        if User.objects.filter(username=username):
            messages.error(request, "Le Username n'est disponible")
            return redirect('signup')

        if len(password1) < 8:
            messages.error(request, "Le mots de pass est trop court")
            return redirect('signup')

        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                        password=password1)
        user.save()
        messages.success(request, "You succefully register ")
        return redirect('connexion')
    return render(request, "signup.html")


def connexion(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password1 = request.POST['password1']
            user = authenticate(username=username, password=password1)
            if user is not None and user.is_active:
                login(request, user)
                username = user.username
                return redirect('product')
            else:
                messages.error(request, "Mauvaise authentification")
                return redirect('connexion')
    else:
        return redirect('product')

    return render(request, "login.html")


@login_required(login_url=connexion)
def signout(request):
    logout(request)
    messages.success(request, 'vous ets bien deconnecter')
    return render(request, 'login.html')


@login_required(login_url=connexion)
def dash(request):
    return render(request, 'dashboard.html')
