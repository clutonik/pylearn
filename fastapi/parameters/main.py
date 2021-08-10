from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

# ---------------
#  PATH Parameters
# ---------------
@app.get("/product/{product_id}")
def read_product(product_id: int):
    return {"product_id": product_id}

# ---------------
# Path Parameter (metadata and number validations)
# ---------------
# Note: ... marks it as required
@app.get("/product/{product_id}/metadata")
def read_product_with_metadata(
    product_id: int = Path(..., title="Product ID", 
                            description="The product identifier",
                            ge=1)
):
    return {"product_id": product_id }
    

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

# ---------------
# QUERY Parameters (additional validations)
# ---------------
# Note: Here Query() is used to define a query parameter and 
# its first argument is the default value and min_length is 
# the minimum length of the value which acts as a validator.
@app.get("/items/additional")
async def read_items_additional(q: Optional[str] = Query(None, min_length=3, max_length=10)):
    results = { "items": [{ "item_id": "test"}] }
    if q:
        results.update({"q": q})
    return results

# ---------------
# QUERY Parameters (add more metadata)
# ---------------
# Note: title and description will be shown in 
@app.get("/items/additional/metadata")
async def read_items_additional_metadata(
    q: Optional[str] = Query(
        None,
        title="Query", 
        description="Query description")):
    return {"q": q}

# ---------------
# QUERY Parameters (deprecated query parameters)
# ---------------
# Note: You can use deprecated query parameters using below ways:
@app.get("/items/deprecated")
async def read_items_deprecated(
    q: Optional[str] = Query(
        None, 
        title="Query", 
        description="Query description",
        deprecated=True)
    ):
    return {"q": q}