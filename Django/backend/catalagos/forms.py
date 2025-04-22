from django import forms
from django.forms import ModelForm
from .models import Usuario, User
from django.contrib.auth.forms import BaseUserCreationForm

class UsuarioForm(ModelForm):

    clave = forms.CharField(label="clave", widget=forms.PasswordInput)
    class Meta:
        model =Usuario
        fields =  [ 'nombreCompleto','nombreUsuario','correo' ,'fechaNacimiento','direccion']



