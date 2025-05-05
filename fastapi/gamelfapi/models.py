from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, Float
from .database import Base

# Oracle



class Categoria(Base):
    __tablename__ = "catalagos_categoria"
    categoria_seq = Sequence("categoria_seq", start=1, increment=1)
    juego_seq = Sequence("juego_seq", start=1, increment=1)
    idCategoria = Column(Integer, categoria_seq, primary_key=True, server_default=categoria_seq.next_value())
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200))

class Juegos(Base):
    __tablename__ = "catalagos_juego"
    juego_seq = Sequence("juego_seq", start=1, increment=1)
    idjuego = Column(Integer, juego_seq, primary_key=True, server_default=juego_seq.next_value())
    nombre = Column(String(60), index=True)
    descripcion = Column(String(1000))
    precio = Column(Integer)
    image = Column(String(100))
    categoria_id = Column(Integer, ForeignKey("catalagos_categoria.idCategoria"))
    imagen = Column(String(100))
    
    
# SQLite
# class Categoria(Base):
#     __tablename__ = "categoria"
    
#     idCategoria = Column(Integer, primary_key=True)
#     nombre = Column(String(50), nullable=False)
#     descripcion = Column(String(200))

# class Juegos(Base):
#     __tablename__ = "juegos"

#     id = Column(Integer, primary_key=True)
#     nombre = Column(String(60), index=True)
#     descripcion = Column(String(1000))
#     precio = Column(Integer)
#     categoria_id = Column(String, ForeignKey("categoria.idCategoria"))