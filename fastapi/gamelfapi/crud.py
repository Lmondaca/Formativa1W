from sqlalchemy.orm import Session
from . import models, schema

def get_juegos(db: Session):
    return db.query(models.Juegos).all()

def get_juego(db: Session, idjuego: int):
    return db.query(models.Juegos).filter(models.Juegos.idjuego == idjuego).first()

def create_juego(db: Session, juego: schema.JuegosCreate):
    nuevo_juego = models.Juegos(
        nombre=juego.nombre,
        descripcion=juego.descripcion,
        precio=juego.precio,
        categoria_id=juego.categoria_id,
        image=juego.image
    )
    db_juego = models.Juegos(**juego.dict())
    db.add(db_juego)
    db.commit()
    db.refresh(db_juego)
    return db_juego

def update_juego(db: Session, idjuego: int, juego: schema.JuegosCreate):
    db_juego = db.query(models.Juegos).filter(models.Juegos.idjuego == idjuego).first()  # Cambiado a idjuego
    if db_juego:
        for attr, value in juego.dict().items():
            setattr(db_juego, attr, value)
        db.commit()
        db.refresh(db_juego)
    return db_juego

def delete_juego(db: Session, idjuego: int):
    db_juego = db.query(models.Juegos).filter(models.Juegos.idjuego == idjuego).first()
    if db_juego:
        db.delete(db_juego)
        db.commit()
    return db_juego

def get_usuarios(db: Session):
    return db.query(models.Usuarios).all()

def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuarios).filter(models.Usuarios.id == usuario_id).first()

def create_usuario(db: Session, usuario: schema.UsuariosCreate):
    db_usuario = models.Usuarios(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schema.UsuariosCreate):
    usuario = db.query(models.Usuarios).filter(models.Usuarios.id == usuario_id).first()
    if usuario:
        for attr, value in usuario.dict().items():
            setattr(usuario, attr, value)
        db.commit()
        db.refresh(usuario)
    return usuario

def delete_usuario(db: Session, usuario_id: int):
    usuario = db.query(models.Usuarios).filter(models.Usuarios.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario
