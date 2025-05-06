from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

class UserType(str, enum.Enum):
    estudiante = "estudiante"
    tutor = "tutor"
    administrador = "administrador"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    contrasena = Column(String, nullable=False)
    tipo = Column(Enum(UserType), nullable=False)
