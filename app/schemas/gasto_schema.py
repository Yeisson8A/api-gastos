from pydantic import BaseModel
from datetime import date

class GastoBase(BaseModel):
    fecha: date
    descripcion: str
    categoria: str
    monto: float

class GastoCreate(GastoBase):
    pass

class GastoUpdate(GastoBase):
    pass

class GastoOut(GastoBase):
    id: int

    class Config:
        from_attributes = True