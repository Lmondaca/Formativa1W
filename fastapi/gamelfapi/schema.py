from pydantic import BaseModel
from datetime import date
# from sqlalchemy import Date


class JuegosBase(BaseModel):
    nombre: str
    descripcion: str
    precio: int
    categoria_id: int
    image: str
    
class JuegosCreate(JuegosBase):
    pass

class Juegos(JuegosBase):
    idjuego: int
    
    class Config:
        from_attributes = True

class UsuariosBase(BaseModel):
    id: int
    nombreCompleto: str
    nombreUsuario: str
    correo: str
    # clave: str
    fechaNacimiento: date
    direccion: str
    # user_id: int

class UsuariosCreate(UsuariosBase):
    pass

class Usuarios(UsuariosBase):
    id: int
    
    class Config:
        from_attributes = True
