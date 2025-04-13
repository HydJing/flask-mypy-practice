from pydantic import BaseModel

class HelloInput(BaseModel):
    name: str

class HelloResponse(BaseModel):
    message: str
