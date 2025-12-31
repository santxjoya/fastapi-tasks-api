from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password 

def create_user(db: Session, email: str, password: str) -> User:
    hashed_password = hash_password(password)
    user = User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, user: User, password: str | None = None) -> User:
    if password:
        user.hashed_password = hash_password(password)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()
