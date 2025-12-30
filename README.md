# FastAPI Tasks API

API REST para la gestión de tareas, desarrollada con **FastAPI** y **PostgreSQL**, que implementa autenticación mediante **JWT** y un CRUD completo con paginación.

El objetivo del proyecto es entregar una solución **end-to-end**, ejecutable en entorno local, con una arquitectura clara y decisiones técnicas explícitas.

---

# Tecnologías

- Python 3.11.8
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT
- Docker / Docker Compose

---

# Requisitos

- Python 3.11+
- Docker
- Docker Compose

---

# Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

*env*
DB_HOST=localhost
DB_PORT=5432
DB_NAME=technical_test
DB_USER=postgres
DB_PASSWORD=postgres

JWT_SECRET_KEY=supersecretkey
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

---

# Base de datos

La base de datos se ejecuta exclusivamente en entorno local usando Docker.

docker-compose up -d

---

# Migraciones

Las migraciones se ejecutan con Alembic, y se encargan de crear las tablas necesarias, y crear automáticamente un usuario inicial para autenticación.

alembic upgrade head

---

# Usuario inicial

El sistema crea un usuario inicial automáticamente para poder autenticarse:

Email: admin@test.com
Password: admin123

---

# Ejecución del proyecto

Instalar dependencias:

    pip install -r requirements.txt

Ejecutar la aplicación:

    uvicorn app.main:app --reload

---

# Decisiones técnicas iniciales

Se utiliza JWT para autenticación por simplicidad y escalabilidad.

Las contraseñas se almacenan usando hash seguro.

La lógica de negocio se separa de los endpoints para mejorar mantenibilidad.

Se implementará paginación real en los listados.

Se utilizará PostgreSQL como base de datos relacional.
