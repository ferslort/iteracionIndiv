from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import FormLogin, FomRegister
from django.contrib.auth import authenticate, login, logout
from users.models import User

# Create your views here.


def user_page(request):
    users = User.objects.all()
    return render(request, 'users.html', {
        'users': users
    })


def index_page(request):

    users = User.objects.all()

    return render(request, 'index.html', {
        'users': users
    })


def register_page(request):

    form = FomRegister()
    if request.method == 'POST':
        form = FomRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'register.html', {
        'form': form
    })


def page_login(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('index')
        else:
            messages.warning(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html', {
        'form': form,
    })


def logout_user(request):
    logout(request)
    return redirect('index')
