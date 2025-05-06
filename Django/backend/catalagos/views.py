from decimal import ROUND_DOWN, Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego, Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers  import make_password
import requests
# from django.contrib.auth.forms import BaseUserCreationForm

# Create your views here.

def catalogo(request):
    #para agregar elementos desde la BD
    contexto = {'saludo': 'variable para usar en la vista'}
    #controlar la sesion
    return render(request, 'index.html', contexto)

def categoria(request):
    return render(request, 'categoria.html')

def mostrar(request, id):
    #lista de libros que se obtiene de la base de datos
    juegos = Juego.objects.all()
    if id >=0 and id < len(juegos):
        contexto = {
            'juego': juegos[id]
        }
        return render(request, 'mostrar.html', contexto)
    else:
        return redirect('carrera')

def carrera(request):
    juegos = Juego.objects.filter(categoria_id=1)
    lista_juego = obtenerDolar(juegos)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': lista_juego,
       
    }
    return render(request, 'carreras.html', contexto)

def obtenerDolar(juegos):
    try:
        precioDolar = dict()
        lista_juego = list()
        response = requests.get("https://cl.dolarapi.com/v1/cotizaciones/usd")
        dolar = response.json()
        montoDolar = Decimal(dolar['compra']).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        print( Decimal(dolar['compra']).quantize(Decimal('.01'), rounding=ROUND_DOWN))
        for juego in juegos:
            precioDolar[juego.nombre]=Decimal((juego.precio)/montoDolar).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            # precioDolar[juego.nombre]=Decimal(212).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            juegos2 = {
                'nombre': juego.nombre,
                'image': juego.image,
                'descripcion': juego.descripcion,
                'precio': juego.precio,
                'precioDolar':  precioDolar[juego.nombre]
            }
            lista_juego.append(juegos2)
        #     print(juego)
        # print(precioDolar)
    except:
        print('error')
    return lista_juego

def disparo(request):
    juegos = Juego.objects.filter(categoria_id=3)
    lista_juego = obtenerDolar(juegos)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': lista_juego
    }    
    return render(request, 'disparos.html', contexto)

def pelea(request):
    juegos = Juego.objects.filter(categoria_id=4)
    lista_juego = obtenerDolar(juegos)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': lista_juego
    }        
    return render(request, 'peleas.html', contexto)

def plataforma(request):
    juegos = Juego.objects.filter(categoria_id=5)
    lista_juego = obtenerDolar(juegos)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': lista_juego
    }    
    return render(request, 'plataforma.html', contexto)

def rol(request):
    juegos = Juego.objects.filter(categoria_id=2)
    lista_juego = obtenerDolar(juegos)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': lista_juego
    }    
    return render(request, 'rol.html', contexto)

def login(request):
    return render(request, 'login.html')

def registro(request):
    form = UsuarioForm()
    
    rendered_form_usuario = form.render("form_usuario.html")
    
    datos = {
        'form': rendered_form_usuario,
        

    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            user_form = User.objects.create_user(username=request.POST.get('nombreUsuario'), first_name=request.POST.get('nombreCompleto'), email=request.POST.get('correo'), password=request.POST.get('clave'))
            user = user_form.save()
            # user1 = get_object_or_404(User, email=request.POST.get('correo'))
            formulario.clave = make_password(request.POST.get('clave'))
            usuario = formulario.save()
            user1 = get_object_or_404(User, email=request.POST.get('correo'))
            usuario.user = user1
            usuario.save()
            datos['mensaje']= "Guardados correctamente"
            return redirect('registro')
 
    return render(request, 'registro.html', datos)

@login_required
def perfil(request):
    user = get_object_or_404(Usuario, correo=request.user.email)
    datos = {
        'nombreUser': request.user.username,
        'correo': user.correo,
        'nombreCompleto': user.nombreCompleto,
        'fechaNaci': user.fechaNacimiento,
        'direccion': user.direccion
    }
    return render(request, 'perfil.html', datos)

def crearJuego(request):
    return render(request, 'nuevo-juego.html')


def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    datos = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, instance=usuario)
        if formulario.is_valid:
            formulario.save()

            datos['mensaje']= "Guardados correctamente"
            return redirect('perfil')
    else:
        datos['form']=UsuarioForm(instance=usuario)
    return render(request, 'form_usuario.html', datos)