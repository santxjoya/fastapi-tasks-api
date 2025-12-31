from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db, get_current_user
from app.crud import user as crud_user
from app.schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user_route(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Crear un nuevo usuario.
    """
    existing_user = crud_user.get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return crud_user.create_user(
        db,
        user_in=user_in
    )

@router.get(
    "/",
    response_model=List[UserResponse],
)
def list_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Listar usuarios con paginación.
    """
    return crud_user.get_users(
        db,
        skip=skip,
        limit=limit,
    )

@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Obtener un usuario por ID.
    """
    user = crud_user.get_user_by_id(
        db,
        user_id=user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user

@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
def update_user_route(
    user_id: int,
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Actualizar un usuario existente.
    """
    user = crud_user.get_user_by_id(
        db,
        user_id=user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return crud_user.update_user(
        db,
        user=user,
        user_in=user_in
    )

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_route(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Eliminar un usuario.
    """
    user = crud_user.get_user_by_id(
        db,
        user_id=user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    crud_user.delete_user(
        db,
        user=user
    )
