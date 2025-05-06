from django import forms
from django.forms import ModelForm
from .models import Usuario, User, Categoria
from django.contrib.auth.forms import BaseUserCreationForm

class UsuarioForm(ModelForm):

    clave = forms.CharField(label="clave", widget=forms.PasswordInput)
    class Meta:
        model =Usuario
        fields =  [ 'nombreCompleto','nombreUsuario','correo' ,'fechaNacimiento','direccion']


class JuegosForm(forms.Form):
    nombre = forms.CharField(max_length=60, label='Nombre del juego')
    descripcion = forms.CharField(max_length=1000, label='Descripcion del juego')
    precio = forms.IntegerField(label='Precio del juego', min_value=0)
    categoria = forms.IntegerField(label='Categoria del juego', min_value=0)
    image = forms.ImageField(label='Imagen del juego', required=False)