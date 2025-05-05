from sqlalchemy.orm import Session
from . import models, schema

def get_juegos(db: Session):
    return db.query(models.Juegos).all()

def get_juego(db: Session, juego_id: int):
    return db.query(models.Juegos).filter(models.Juegos.id_juego == juego_id).first()

def create_juego(db: Session, juego: schema.JuegosCreate):
    db_juego = models.Juegos(**juego.dict())
    db.add(db_juego)
    db.commit()
    db.refresh(db_juego)
    return db_juego

def update_juego(db: Session, juego_id: int, juego: schema.JuegosCreate):
    juego = db.query(models.Juegos).filter(models.Juegos.id == juego_id).first()
    if juego:
        for attr, value in juego.dict().items():
            setattr(juego, attr, value)
        db.commit()
        db.refresh(juego)
    return juego

def delete_juego(db: Session, juego_id: int):
    juego = db.query(models.Juegos).filter(models.Juegos.id == juego_id).first()
    if juego:
        db.delete(juego)
        db.commit()
    return juego