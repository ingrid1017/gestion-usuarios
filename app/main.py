from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/usuarios/", response_model=schemas.Usuario)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    return crud.crear_usuario(db, usuario)

@app.get("/usuarios/", response_model=list[schemas.Usuario])
def listar_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.obtener_usuarios(db, skip, limit)

@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def obtener_usuario(usuario_id: int, db: Session = Depends(database.get_db)):
    db_usuario = crud.obtener_usuario_por_id(db, usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario
