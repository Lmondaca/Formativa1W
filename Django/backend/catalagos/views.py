from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego, Usuario
from .forms import UsuarioForm

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
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': juegos
    }
    return render(request, 'carreras.html', contexto)

def disparo(request):
    juegos = Juego.objects.filter(categoria_id=3)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': juegos
    }    
    return render(request, 'disparos.html', contexto)

def pelea(request):
    juegos = Juego.objects.filter(categoria_id=4)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': juegos
    }        
    return render(request, 'peleas.html', contexto)

def plataforma(request):
    juegos = Juego.objects.filter(categoria_id=4)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': juegos
    }    
    return render(request, 'plataforma.html', contexto)

def rol(request):
    juegos = Juego.objects.filter(categoria_id=2)
    contexto = {
        'saludo': 'variable para usar en la vista',
        'juegos': juegos
    }    
    return render(request, 'rol.html', contexto)

def login(request):
    return render(request, 'login.html')

def registro(request):
    form = UsuarioForm()
    rendered_form = form.render("form_usuario.html")
    datos = {
        'form': rendered_form
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            
            datos['mensaje']= "Guardados correctamente"
            return redirect('registro')
 
    return render(request, 'registro.html', datos)


def perfil(request):
    return render(request, 'perfil.html')

def crearJuego(request):
    return render(request, 'nuevo-juego.html')

# def form_usuario(request):
#     form = UsuarioForm()
#     rendered_form = form.render("form_usuario.html")
#     datos = {
#         'form': rendered_form
#     }
#     if request.method == 'POST':
#         formulario = UsuarioForm(request.POST)
#         if formulario.is_valid:
#             formulario.save()

#             datos['mensaje']= "Guardados correctamente"
#     return render(request, 'registro.html', datos)

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