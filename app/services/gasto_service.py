from sqlalchemy.orm import Session
from app.models import models
from app.schemas import gasto_schema

def get_gastos(db: Session):
    return db.query(models.Gasto).all()

def get_gasto(db: Session, gasto_id: int):
    return db.query(models.Gasto).filter(models.Gasto.id == gasto_id).first()

def create_gasto(db: Session, gasto: gasto_schema.GastoCreate):
    db_gasto = models.Gasto(**gasto.model_dump())
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

def update_gasto(db: Session, gasto_id: int, gasto: gasto_schema.GastoUpdate):
    db_gasto = get_gasto(db, gasto_id)
    if not db_gasto:
        return None
    for key, value in gasto.model_dump().items():
        setattr(db_gasto, key, value)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

def delete_gasto(db: Session, gasto_id: int):
    db_gasto = get_gasto(db, gasto_id)
    if not db_gasto:
        return None
    db.delete(db_gasto)
    db.commit()
    return db_gasto