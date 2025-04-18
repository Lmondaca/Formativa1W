
from django.urls import path
from .views import catalogo, carrera, disparo, pelea, plataforma, rol, login, registro, perfil, crearJuego
urlpatterns = [
    path('inicio', catalogo, name="catalogo"),
    path('carreras', carrera, name="carrera"),
    path('disparos', disparo, name="disparo"),
    path('peleas', pelea, name="pelea"),
    path('plataformas', plataforma, name="plataforma"),
    path('rols', rol, name="rol"),
    path('login', login, name="login"),
    path('registro', registro, name="registro"),
    path('perfil', perfil, name="perfil"),
    path('crear-juego', crearJuego, name="crearJuego"),
]