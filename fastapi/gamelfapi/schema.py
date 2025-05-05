from pydantic import BaseModel

class JuegosBase(BaseModel):
    nombre: str
    descripcion: str
    precio: int
    categoria_id: str
    
class JuegosCreate(JuegosBase):
    pass

class Juegos(JuegosBase):
    id: int
    
    class Config:
        from_attributes = True