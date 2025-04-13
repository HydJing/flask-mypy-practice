from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import UserRegistration
from app.database import SessionLocal

class UserAlreadyExistsError(Exception):
    pass

def register_user(db: Session, user_data: UserRegistration) -> User:
    # Check if the user already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise UserAlreadyExistsError(f"User with email {user_data.email} already exists.")
    
    # Register new user
    db_user = User(email=user_data.email, name=user_data.name, is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
