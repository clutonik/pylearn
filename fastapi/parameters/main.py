from fastapi import FastAPI

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
@app.get("/items/")
# NOTE: skip is a required parameter, but limit is not
async def read_products(skip: int, limit: int = 100):
    return {"skip": skip, "limit": limit}