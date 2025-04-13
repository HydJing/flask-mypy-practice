from pydantic import BaseModel, EmailStr

class ProductRegistration(BaseModel):
    name: str
    price: float
    email: EmailStr

# Now, simulating the registration with wrong data types
def register_product(data: dict):
    product = ProductRegistration.model_validate(data)
    return product
