from pydantic import BaseModel, EmailStr, validator

class UserRegistration(BaseModel):
    email: EmailStr
    name: str

    @validator('email')
    def email_domain(cls, v):
        if '@example.com' not in v:
            raise ValueError('Email must be from example.com')
        return v

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    is_active: bool
