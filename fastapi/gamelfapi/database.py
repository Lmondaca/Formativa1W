from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
# SQLALCHEMY_DATABASE_URL = "sqlite:///./juegos.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

load_dotenv() 

un = "WEB1"
pw = os.getenv("DATABASE_PASSWORD")
cd = os.getenv("WALLET_LOCATION")
wloc = os.getenv("WALLET_LOCATION")
wpw  = os.getenv("WALLET_PASSWORD")
cs ="cmb0n6s7y4so8ofj_high"

engine = create_engine(
    f'oracle+oracledb://:@',
    connect_args={
        "user": un,
        "password": pw,
        "dsn": cs,
        "config_dir": cd,
        "wallet_location": wloc,
        "wallet_password": wpw,

    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
