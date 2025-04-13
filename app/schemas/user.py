from typing import Optional, List
from pydantic import BaseModel, HttpUrl

class UserProfile(BaseModel):
    bio: Optional[str]
    website: Optional[HttpUrl]

class UserModel(BaseModel):
    id: int
    name: str
    email: Optional[str]
    is_active: bool
    tags: List[str]
    profile: Optional[UserProfile]

class UserResponse(BaseModel):
    data: UserModel
