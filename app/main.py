from fastapi import FastAPI
from app.db.config import engine, Base
from app.routes import gasto_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gastos",
    version="1.0.0"
)

# Agregar rutas
app.include_router(gasto_routes.router)