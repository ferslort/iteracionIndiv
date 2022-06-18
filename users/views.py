from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

from .models import Cliente
from .forms import RegisterForm


def user_page(request):
    return render(request, 'users.html')

def index_page(request):

    users = Cliente.objects.all()

    return render(request, 'index.html', {
        'users': users
    })


def register_page(request):

    form = RegisterForm()

    if request.method == 'POST':
        name = request.POST['name']
        lastName = request.POST['lastName']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        client = Cliente(
            name = name,
            lastName = lastName,
            address=address,
            phone=phone,
            email=email,
            password = password
        )

        client.save()
        messages.success(request, 'Registro Exitoso')


    return render(request, 'register.html', {
        'form': form
    })

