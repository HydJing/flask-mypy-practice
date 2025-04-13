from typing import Optional, Dict, Any, List
from sqlalchemy.orm import Session
from app.models.user import User
from app.database import SessionLocal

def get_user_by_id(user_id: int) -> Dict[str, Any]:
    # Simulate DB lookup
    if user_id == 1:
        return {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "is_active": True,
            "tags": ["admin", "tester"],
            "profile": {
                "bio": "Loves Flask.",
                "website": "https://alice.dev"
            }
        }
    return {
        "id": user_id,
        "name": "Unknown",
        "email": None,
        "is_active": False,
        "tags": [],
        "profile": None
    }

def get_users(db: Session) -> List[User]:
    users = db.query(User).all()
    # return users  # Should return a list of User objects, but we'll return a string instead
    return "this is a string"  # Error: returning a string instead of List[User]

def get_user_by_id(db: Session, user_id: int) -> str:
    # Should return a User, but we're returning a string
    user = db.query(User).filter(User.id == user_id).first()
    return user  # Error: Expected User, but returning string
