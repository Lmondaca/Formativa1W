from django.shortcuts import render, redirect
from .models import Juego

# Create your views here.
def catalogo(request):
    #para agregar elementos desde la BD
    
    contexto = {'saludo': 'variable para usar en la vista'}
    return render(request, 'index.html', contexto)

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
    return render(request, 'registro.html')


def perfil(request):
    return render(request, 'perfil.html')

def crearJuego(request):
    return render(request, 'nuevo-juego.html')