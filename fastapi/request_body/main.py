from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example:1 

# Pydantic model for a product
class Product(BaseModel):
    name: str
    price: float
    stock: int

# Create a POST /products endpoint and accept Product
@app.post("/products")
async def create_product(product: Product):
    return {'response': product}

# Example:2
# Create pydantic model for user
class User(BaseModel):
    name: str
    password: str
    id: int = None
    age: int = None
    address: str = None

# Create a POST /users endpoint and accept User
@app.post("/users")
async def create_user(user: User):
    return {'response': user}