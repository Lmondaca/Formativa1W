from pydantic import BaseModel

class JuegosBase(BaseModel):
    nombre: str
    descripcion: str
    precio: int
    categoria_id: int
    
class JuegosCreate(JuegosBase):
    pass

class Juegos(JuegosBase):
    idjuego: int
    
    class Config:
        from_attributes = True