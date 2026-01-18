from sqlalchemy import Column, Integer, String, Float, Date
from app.db.config import Base

class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    descripcion = Column(String(255), nullable=False)
    categoria = Column(String(100), nullable=False)
    monto = Column(Float, nullable=False)