from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.tasks import router as tasks_router
# from app.api.user import router as users_router

app = FastAPI(
    title="FastAPI Tasks API",
    description="API REST para gestión de tareas con autenticación JWT",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(tasks_router)
# app.include_router(users_router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
