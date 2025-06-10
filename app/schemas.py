from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel
from typing import Optional 

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


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    contrasena: Optional[str] = None
    tipo: Optional[UserType] = None

