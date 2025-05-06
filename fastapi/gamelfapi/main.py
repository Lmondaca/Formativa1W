from typing import Union, List
from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import models, schema, crud
from .database import SessionLocal, engine, Base

from fastapi.middleware.cors import CORSMiddleware


# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001", "http://localhost:8001"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

        
@app.post("/juegos2/", response_model=schema.Juegos)
def create_juego2(
    nombre: str,
    descripcion: str,
    precio: int,
    categoria_id: int,
    image: str,
    db: Session = Depends(get_db)
):

    image_aux = f"img/{image.filename}"

    # Crea el juego en la base de datos
    nuevo_juego = schema.JuegosCreate(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        categoria_id=categoria_id,
        image=image_aux
    )
    return crud.create_juego(db, nuevo_juego)        
               
        
@app.post("/juegos/", response_model=schema.Juegos)
def create_juego(
    nombre: str,
    descripcion: str,
    precio: int,
    categoria_id: int,
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Guarda la imagen en el servidor
    image_path = f"../../Django/backend/catalagos/static/img/{image.filename}"
    with open(image_path, "wb") as f:
        f.write(image.file.read())
    
    image_aux = f"img/{image.filename}"

    # Crea el juego en la base de datos
    nuevo_juego = schema.JuegosCreate(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        categoria_id=categoria_id,
        image=image_aux
    )
    return crud.create_juego(db, nuevo_juego)

@app.get("/juegos/", response_model=List[schema.Juegos])
def listar_juegos(db: Session = Depends(get_db)):
    return crud.get_juegos(db)

@app.get("/juegos/{idjuego}", response_model=schema.Juegos)
def obtener_juego(idjuego: int, db: Session = Depends(get_db)):
    jue = crud.get_juego(db, idjuego)
    if jue is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return jue

@app.put("/juegos/{idjuego}", response_model=schema.Juegos)
def actualizar_juego(idjuego: int, juego: schema.JuegosCreate, db: Session = Depends(get_db)):
    jue = crud.update_juego(db, idjuego, juego)
    if jue is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return jue

@app.delete("/juegos/{idjuego}", response_model=schema.Juegos)
def eliminar_juego(idjuego: int, db: Session = Depends(get_db)):
    jue = crud.delete_juego(db, idjuego)
    if jue is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return jue

@app.post("/usuarios/", response_model=schema.Usuarios)
def create_usuario(usuario: schema.UsuariosCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db, usuario)

@app.get("/usuarios/", response_model=List[schema.Usuarios])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.get_usuarios(db)

@app.get("/usuarios/{usuario_id}", response_model=schema.Usuarios)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usu = crud.get_usuario(db, usuario_id)
    if usu is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usu

@app.put("/usuarios/{usuario_id}", response_model=schema.Usuarios)
def actualizar_usuario(usuario_id: int, usuario: schema.UsuariosCreate, db: Session = Depends(get_db)):
    usu = crud.update_usuario(db, usuario_id, usuario)
    if usu is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usu

@app.delete("/usuarios/{usuario_id}", response_model=schema.Usuarios)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usu = crud.delete_usuario(db, usuario_id)
    if usu is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usu
