from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1234@localhost/gestion_usuarios_db") 
engine = create_engine(SQLALCHEMY_DATABASE_URL) 
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db(): 
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close()