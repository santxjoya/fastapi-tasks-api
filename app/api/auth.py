from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import LoginRequest, TokenResponse, UserCreate, UserResponse
from app.core.security import verify_password, create_access_token
from app.db.session import SessionLocal
from app.models.user import User
from app.api.deps import get_db
from app.crud import user as crud_user


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse, status_code=201)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    print(user_in)
    existing_user = crud_user.get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db, user_in.email, user_in.password)


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    db: Session = SessionLocal()

    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(
        data.password, user.hashed_password
    ):
        db.close()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )

    token = create_access_token({"sub": user.id})
    db.close()

    return {"access_token": token}
