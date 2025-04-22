from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria
    
class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca Vehixulo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
    
class Juego(models.Model):
    idJuego = models.IntegerField(primary_key=True, verbose_name='Id del juego')
    nombre =models.CharField(max_length=60, verbose_name='nombre del juego')
    descripcion = models.CharField(max_length=1000 , verbose_name='descripcion del juego')
    precio = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio del juego')
    image = models.CharField(max_length=100, verbose_name='direccion de la portada del juego')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='juegos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE ,null=True)
    nombreCompleto =models.CharField(max_length=60, verbose_name='nombre completo del usuario')
    nombreUsuario =models.CharField(max_length=60, verbose_name='Alias del usuario')
    correo = models.EmailField(unique=True, verbose_name='correo personal')
    clave = models.CharField(max_length=128 , verbose_name='password')
    fechaNacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    direccion = models.CharField(max_length=300 , verbose_name='direccion')
    

    def __str__(self):
        return self.nombreUsuario
    