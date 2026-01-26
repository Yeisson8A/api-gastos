# Api para gestión de gastos en FastAPI y PostgreSQL contenerizada
Proyecto de desarrollo de una API para la gestión de gastos, usando las librerías Uvicorn, SQL Alchemy y FastAPI, además teniendo como base de datos PostgreSQL; todo esto contenerizado mediante Docker.

## Requisitos
- Docker y Docker Compose
- Python 3.8+

# Environment
- **DB_HOST:** Host del servidor de base de datos, o del contenedor en Docker, por ejemplo: postgresql
- **DB_PORT:** Puerto del servidor de base de datos, para PostgreSQL el puerto por defecto es 5432
- **DB_NAME:** Nombre de la base de datos
- **DB_USER:** Usuario del servidor de base de datos
- **DB_PASSWORD:** Contraseña del usuario del servidor de base de datos

### Crear la red Docker (una sola vez)
`docker network create gastos-net`

### Conectar el contenedor PostgreSQL a la red
`docker network connect gastos-net postgresql`

### Construir la imagen
`docker-compose build`

### Levantar todo
`docker-compose up -d`

## Acceso
- **API**: `http://localhost:8000`
- **Swagger**: `http://localhost:8000/docs`
- **PostgreSQL**: `localhost:5432`
