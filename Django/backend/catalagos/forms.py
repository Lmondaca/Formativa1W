from django import forms
from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):

    class Meta:
        model =Usuario
        fields = ['nombreCompleto','nombreUsuario','correo','clave','fechaNacimiento','direccion']