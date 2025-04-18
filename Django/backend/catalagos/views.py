from django.shortcuts import render

# Create your views here.
def catalogo(request):
    return render(request, 'index.html')

def categoria(request):
    return render(request, 'categoria.html')

def carrera(request):
    return render(request, 'carreras.html')

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