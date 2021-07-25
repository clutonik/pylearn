from fastapi import FastAPI

from typing import Optional


app = FastAPI()

# ---------------
#  PATH Parameters
# ---------------
@app.get("/product/{product_id}")
def read_product(product_id: int):
    return {"product_id": product_id}

# ---------------
#  QUERY Parameters (with default values)
# ---------------
@app.get("/products/")
async def read_products(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}

# ---------------
# QUERY Parameters (required to be defined)
# ---------------
@app.get("/items/required")
# NOTE: skip is a required parameter, but limit is not
async def read_products(skip: int, limit: int = 100):
    return {"skip": skip, "limit": limit}

# ---------------
# QUERY Parameters (optional)
# ---------------
# NOTE: q is an optional parameter and its default value is None
@app.get("/items/optional")
async def read_optional_items(skip: int = 0, q: Optional[str] = None, limit: int = 100):
    if q:
        return {"skip": skip, "limit": limit, "q": q}
    return {"skip": skip, "limit": limit}

# ---------------
# QUERY Parameters (booleans)
# ---------------
# Note: You can use bool query parameters using below ways:
# 1. http://localhost:8000/items/booleans?all=False
# 2. http://localhost:8000/items/booleans?all=0
# 3. http://localhost:8000/items/booleans?all=yes
@app.get("/items/booleans")
async def read_items_booleans(skip: int = 0, all: bool = True):
    if all:
        return {"products": "all"}

    return {"products": "some"}