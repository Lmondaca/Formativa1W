from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base  # Importación correcta

class Categoria(Base):
    __tablename__ = "categorias"
    
    idCategoria = Column(Integer, primary_key=True, index=True)
    nombreCategoria = Column(String(50), nullable=False)
    descripcion = Column(String(255))
    
    juegos = relationship("Juego", back_populates="categoria")

class Juego(Base):
    __tablename__ = "juegos"
    
    idJuego = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500))
    precio = Column(Integer, nullable=False)
    stock = Column(Integer, default=0)
    categoria_id = Column(Integer, ForeignKey("categorias.idCategoria"))
    
    categoria = relationship("Categoria", back_populates="juegos")