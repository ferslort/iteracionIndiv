from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FomRegister (UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']


class FormLogin (forms.Form):

    username = forms.CharField(
        label='Usuario',
        required=True
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput()
    )


class RegisterForm (forms.Form):

    name = forms.CharField(
        label='Nombre',
        required=True
    )
    lastName = forms.CharField(
        label='Apellido',
        required=True
    )
    address = forms.CharField(
        label='Dirección',
        required=True
    )
    phone = forms.CharField(
        label='Teléfono',
        required=True
    )
    email = forms.EmailField(
        label='Email',
        required=True
    )
    password = forms.CharField(
        label='Contraseña',
        required=True
    )
