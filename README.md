# Api para gestión de gastos en FastAPI y PostgreSQL contenerizada
Proyecto de desarrollo de una API para la gestión de gastos, usando las librerías Uvicorn, SQL Alchemy y FastAPI, además teniendo como base de datos PostgreSQL; todo esto contenerizado mediante Docker.

## Requisitos
- Docker y Docker Compose
- Python 3.8+

### Construir la imagen
`docker-compose build`

### Levantar todo
`docker-compose up -d`

## Acceso
- **API**: `http://localhost:8000`
- **Swagger**: `http://localhost:8000/docs`
- **PostgreSQL**: `localhost:5432`
