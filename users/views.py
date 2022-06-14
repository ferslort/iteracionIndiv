from django.shortcuts import render

# Create your views here.

from .models import UserCustom


def user_page(request):
    return render(request, 'users.html')

def index_page(request):

    users = UserCustom.objects.all()

    return render(request, 'index.html', {
        'users': users
    })
