from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nombreCategoria: str
    descripcion: str = None
    
    class Config:
        # Para Pydantic v2
        from_attributes = True
        # Para Pydantic v1
        # orm_mode = True

class CategoriaCreate(CategoriaBase):
    pass

class JuegoBase(BaseModel):
    idJuego: int
    nombre: str
    descripcion: str = None
    precio: int
    stock: int = 0
    categoria_id: int
    
    class Config:
        # Para Pydantic v2
        from_attributes = True
        # Para Pydantic v1
        # orm_mode = True

class JuegoCreate(BaseModel):
    nombre: str
    descripcion: str = None
    precio: int
    stock: int = 0
    categoria_id: int