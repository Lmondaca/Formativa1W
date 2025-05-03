from fastapi import FastAPI
from app.routers import categorias, juegos  # <-- Importar los routers

app = FastAPI()

app.include_router(categorias.router)
app.include_router(juegos.router)

@app.get("/")
def root():
    return {"message": "API de Tienda de Videojuegos"}