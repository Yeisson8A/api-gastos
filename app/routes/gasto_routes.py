from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import SessionLocal
from app.schemas import gasto_schema
from app.services import gasto_service

router = APIRouter(prefix="/gastos", tags=["Gastos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[gasto_schema.GastoOut])
def listar_gastos(db: Session = Depends(get_db)):
    return gasto_service.get_gastos(db)

@router.post("/", response_model=gasto_schema.GastoOut)
def crear_gasto(gasto: gasto_schema.GastoCreate, db: Session = Depends(get_db)):
    return gasto_service.create_gasto(db, gasto)

@router.put("/{gasto_id}", response_model=gasto_schema.GastoOut)
def actualizar_gasto(gasto_id: int, gasto: gasto_schema.GastoUpdate, db: Session = Depends(get_db)):
    db_gasto = gasto_service.update_gasto(db, gasto_id, gasto)
    if not db_gasto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return db_gasto

@router.delete("/{gasto_id}")
def eliminar_gasto(gasto_id: int, db: Session = Depends(get_db)):
    db_gasto = gasto_service.delete_gasto(db, gasto_id)
    if not db_gasto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return {"ok": True}