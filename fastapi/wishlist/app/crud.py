from sqlalchemy.orm import Session
from models import Categoria, Juego, Usuario

# Operaciones para Categorías
def crear_categoria(db: Session, categoria: CategoriaBase):
    db_categoria = Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categorias(db: Session):
    return db.query(Categoria).all()

# Operaciones para Juegos
def crear_juego(db: Session, juego: JuegoBase):
    db_juego = Juego(**juego.dict())
    db.add(db_juego)
    db.commit()
    db.refresh(db_juego)
    return db_juego

def obtener_juegos_por_categoria(db: Session, categoria_id: int):
    return db.query(Juego).filter(Juego.categoria_id == categoria_id).all()

# Operaciones para Usuarios (base)
def crear_usuario(db: Session, usuario: UsuarioBase):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario