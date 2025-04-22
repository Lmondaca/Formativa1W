from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego, Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers  import make_password
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
    juegos = Juego.objects.all()
    # juego1 = {'nombre': 'mario1','imagen':'img/portadamario1.png'}
    # juego2 = {'nombre': 'mario2','imagen':'img/portadamario2.png'}
    # juego3 = {'nombre': 'mario3','imagen':'img/portadamario3.png'}
    # juegos.append(juego1)
    # juegos.append(juego2)
    # juegos.append(juego3)
    contexto = {'saludo': 'variable para usar en la vista',
                'juegos': juegos
                }
    return render(request, 'carreras.html', contexto)

def disparo(request):
    return render(request, 'disparos.html')

def pelea(request):
    return render(request, 'peleas.html')

def plataforma(request):
    return render(request, 'plataforma.html')

def rol(request):
    return render(request, 'rol.html')

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
            usuario = formulario.save(commit=False)
            usuario.user = user
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