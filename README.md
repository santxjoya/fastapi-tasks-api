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

# Endpoints principales

# Auth

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/auth/login` | Obtener token JWT |

## Tareas

| Método | Ruta | Descripción | Autenticación |
|--------|------|-------------|---------------|
| GET | `/tasks/` | Listar tareas con paginación | JWT |
| POST | `/tasks/` | Crear nueva tarea | JWT |
| GET | `/tasks/{id}` | Obtener tarea por ID | JWT |
| PUT | `/tasks/{id}` | Actualizar tarea | JWT |
| DELETE | `/tasks/{id}` | Eliminar tarea | JWT |

---

# Estructura del proyecto

    app/
    ├─ api/ # Routers de endpoints
    ├─ core/ # Configuración y settings
    ├─ crud/ # Lógica de base de datos
    ├─ db/ # Sesión y conexión a DB
    ├─ models/ # Modelos SQLAlchemy
    ├─ schemas/ # Schemas Pydantic
    └─ main.py # Inicialización de la app

---

# Obtener token:

    POST "http://127.0.0.1:8000/auth/login" \
    "Content-Type: application/json" \
    '{"email": "admin@test.com", "password": "admin123"}'

---

# Crear tarea:

    POST "http://127.0.0.1:8000/tasks/" \
    "Authorization: Bearer <TOKEN>" \
    "Content-Type: application/json" \
    '{"title": "Mi tarea", "description": "Descripción"}'

# Notas finales

Se añadio registro de usuarios.

# Actualizaciones futuras

Reestablecimiento de contraseña por medio de Correo electronico