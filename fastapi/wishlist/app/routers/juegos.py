from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Juego, Categoria
from app.schemas import JuegoBase, JuegoCreate

router = APIRouter(prefix="/juegos", tags=["juegos"])

@router.post("/", response_model=JuegoBase)
def crear_juego(juego: JuegoCreate, db: Session = Depends(get_db)):
    # Verificar si la categoría existe
    categoria = db.query(Categoria).filter(Categoria.idCategoria == juego.categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="La categoría no existe")
    
    db_juego = Juego(
        nombre=juego.nombre,
        descripcion=juego.descripcion,
        precio=juego.precio,
        stock=juego.stock,
        categoria_id=juego.categoria_id
    )
    db.add(db_juego)
    db.commit()
    db.refresh(db_juego)
    return db_juego

@router.get("/", response_model=list[JuegoBase])
def obtener_juegos(db: Session = Depends(get_db)):
    juegos = db.query(Juego).all()
    return juegos

@router.get("/{juego_id}", response_model=JuegoBase)
def obtener_juego(juego_id: int, db: Session = Depends(get_db)):
    juego = db.query(Juego).filter(Juego.idJuego == juego_id).first()
    if juego is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return juego

@router.put("/{juego_id}", response_model=JuegoBase)
def actualizar_juego(juego_id: int, juego: JuegoCreate, db: Session = Depends(get_db)):
    db_juego = db.query(Juego).filter(Juego.idJuego == juego_id).first()
    if db_juego is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    
    # Verificar si la categoría existe
    if juego.categoria_id:
        categoria = db.query(Categoria).filter(Categoria.idCategoria == juego.categoria_id).first()
        if not categoria:
            raise HTTPException(status_code=404, detail="La categoría no existe")
    
    db_juego.nombre = juego.nombre
    db_juego.descripcion = juego.descripcion
    db_juego.precio = juego.precio
    db_juego.stock = juego.stock
    db_juego.categoria_id = juego.categoria_id
    
    db.commit()
    db.refresh(db_juego)
    return db_juego

@router.delete("/{juego_id}")
def eliminar_juego(juego_id: int, db: Session = Depends(get_db)):
    db_juego = db.query(Juego).filter(Juego.idJuego == juego_id).first()
    if db_juego is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    
    db.delete(db_juego)
    db.commit()
    return {"message": "Juego eliminado correctamente"}