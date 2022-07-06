from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FomRegister (UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']

        USERNAME_FIELD = 'email'

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

    pass
