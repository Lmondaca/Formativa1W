import requests
from .models import Categoria

BASE_URL = 'http://127.0.0.1:8000'

def listar_juegos():
    try:
        r = requests.get(f"{BASE_URL}/juegos/")
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return []

def create_juego(data):
    print("comenzando create_juego")
    # Crea una copia de los datos para no modificar el original
    data_copy = data.copy()
    
    # Maneja el objeto Categoria
    if 'categoria' in data_copy and isinstance(data_copy['categoria'], Categoria):
        print("entrando al if de objetos")
        # Convierte el ID a string, ya que la API espera un string
        data_copy['categoria'] = str(data_copy['categoria'].idCategoria)
        del data_copy['categoria']
    
    # Verifica que todos los campos esperados estén presentes
    required_fields = ['nombre', 'descripcion', 'precio', 'categoria']
    for field in required_fields:
        if field not in data_copy:
            print(f"Falta el campo requerido: {field}")
    
    print("Datos enviados a la API:", data_copy)  # Para depuración
    
    data_copy2 = {
        "nombre": data_copy["nombre"],
        "descripcion": data_copy["descripcion"],
        "precio": data_copy["precio"],
        "categoria_id": data_copy["categoria"],
        "image": data_copy["image"].name
    }
    print(data_copy2)
    
    try:
        print("antes de post a fastapi")
        r = requests.post(f"{BASE_URL}/juegos2/", json=data_copy2)
        print("despues de post a fastapi")
        r.raise_for_status()
        print(r.raise_for_status())
        return r.json()
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
        if e.response.status_code == 422:
            error_detail = e.response.json()
            print("Detalle del error de validación:", error_detail)
        raise
    
def actualizar_juego(idjuego, data):
    # Crea una copia de los datos para no modificar el original
    data_copy = data.copy()
    
    # Maneja el objeto Categoria
    if 'categoria' in data_copy and isinstance(data_copy['categoria'], Categoria):
        # Convierte el ID a string, ya que la API espera un string
        data_copy['categoria_id'] = str(data_copy['categoria'].idCategoria)
        del data_copy['categoria']
    
    r = requests.put(f"{BASE_URL}/juegos/{idjuego}", json=data_copy)
    r.raise_for_status()
    return r.json()

def obtener_juego(idjuego):
    r = requests.get(f"{BASE_URL}/juegos/{idjuego}")
    r.raise_for_status()
    return r.json()

def eliminar_juego(idjuego):
    r = requests.delete(f"{BASE_URL}/juegos/{idjuego}")
    r.raise_for_status()
    return r.json()