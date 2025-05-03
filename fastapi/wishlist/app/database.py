# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de Oracle - formato correcto
DATABASE_URL = "oracle+oracledb://WEB1:ClaveOracle123@adb.sa-valparaiso-1.oraclecloud.com:1522/g0022de2e3ebc85_cmb0n6s7y4so8ofj_high.adb.oraclecloud.com"

# Alternativa: usar SQLite para desarrollo/pruebas
# DATABASE_URL = "sqlite:///./wishlist.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Función para proporcionar la dependencia de la sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()