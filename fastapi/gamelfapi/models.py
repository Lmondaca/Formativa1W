from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, Float, DateTime, Date
from .database import Base


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
    # imagen = Column(String(100))
    
class Usuarios(Base):
    __tablename__ = "catalagos_usuario"
    usuario_seq = Sequence("usuario_seq", start=1, increment=1)
    id = Column(Integer, primary_key=True, server_default=usuario_seq.next_value())
    nombreCompleto = Column("NOMBRECOMPLETO", String(60), index=True)
    nombreUsuario = Column("NOMBREUSUARIO", String(60), unique=True)
    correo = Column(String(100), unique=True)
    # clave = Column(String(128))
    fechaNacimiento = Column("FECHANACIMIENTO", Date)
    direccion = Column(String(300))
    # user_id = Column(Integer, ForeignKey("auth_user.id"))
    