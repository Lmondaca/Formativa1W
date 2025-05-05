from typing import Union, List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import models, schema, crud
from .database import SessionLocal, engine, Base

from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

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
        
@app.post("/juegos/", response_model=schema.Juegos)
def create_juego(juego: schema.JuegosCreate, db: Session = Depends(get_db)):
    return crud.create_juego(db, juego)

@app.get("/juegos/", response_model=List[schema.Juegos])
def listar_juegos(db: Session = Depends(get_db)):
    return crud.get_juegos(db)

@app.get("/juegos/{juego_id}", response_model=schema.Juegos)
def obtener_juego(juego_id: int, db: Session = Depends(get_db)):
    jue = crud.get_juego(db, juego_id)
    if jue is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return jue

@app.put("/juegos/{juego_id}", response_model=schema.Juegos)
def actualizar_juego(juego_id: int, juego: schema.JuegosCreate, db: Session = Depends(get_db)):
    jue = crud.update_juego(db, juego_id, juego)
    if jue is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return jue

@app.delete("/juegos/{juego_id}", response_model=schema.Juegos)
def eliminar_juego(juego_id: int, db: Session = Depends(get_db)):
    jue = crud.delete_juego(db, juego_id)
    if jue is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return jue