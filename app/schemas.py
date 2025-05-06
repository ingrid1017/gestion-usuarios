from pydantic import BaseModel
from enum import Enum

class UserType(str, Enum):
    estudiante = "estudiante"
    tutor = "tutor"
    administrador = "administrador"

class UsuarioBase(BaseModel):
    nombre: str
    contrasena: str
    tipo: UserType

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
