from django import forms




class RegisterForm (forms.Form):

    name = forms.CharField(
      label='Nombre',
       required = True
    )
    lastName = forms.CharField(
      label= 'Apellido',
       required = True
    )
    address = forms.CharField(
     label= 'Dirección',
       required = True
    )
    phone = forms.CharField(
      label= 'Teléfono',
       required = True
    )
    email = forms.EmailField(
        label= 'Email',
       required = True
    )
    password = forms.CharField(
      label= 'Contraseña',
       required = True
    )
