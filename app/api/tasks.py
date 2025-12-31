from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db, get_current_user
from app.crud import task as crud_task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task_in: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Crear una nueva tarea para el usuario autenticado.
    """
    return crud_task.create_task(
        db,
        user_id=current_user.id,
        task_in=task_in,
    )

@router.get(
    "/",
    response_model=List[TaskResponse],
)
def list_tasks(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Listar tareas del usuario autenticado con paginación.
    """
    return crud_task.get_tasks(
        db,
        user_id=current_user.id,
        skip=skip,
        limit=limit,
    )

@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Obtener una tarea por ID.
    """
    task = crud_task.get_task_by_id(
        db,
        task_id=task_id,
        user_id=current_user.id,
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task

@router.put(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    task_id: int,
    task_in: TaskUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Actualizar una tarea existente.
    """
    task = crud_task.get_task_by_id(
        db,
        task_id=task_id,
        user_id=current_user.id,
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return crud_task.update_task(
        db,
        task=task,
        task_in=task_in,
    )

@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Eliminar una tarea.
    """
    task = crud_task.get_task_by_id(
        db,
        task_id=task_id,
        user_id=current_user.id,
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    crud_task.delete_task(db, task=task)
