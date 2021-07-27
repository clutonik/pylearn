#!/usr/bin/env python3
import pydantic

# This file demonstrates use of the pydantic library to define a schema

""" 
Reasons why I am learning this:
 - I am writing this to understand how pydantic works and how I can use it
   with FastAPI to define a schema.
 - Pydantic is the base to understand how FastAPI validates data.
 - The data being sent to your API might be untrusted and you might want to parse it to
   ensure that it has the correct type(str/int etc.). So, this is where pydantic comes in.
"""

# Sample class which is a child of the pydantic BaseModel.
# This is also known as a Model.
class User(pydantic.BaseModel):
    name: str # mandatory field
    id: int # mandatory field
    gender = 'male' # This is an optional field because it has a default value

# Key notes for baseModel:
# 1. When you create an object of this model(class), you need to supply mandatory fields
# 2. When you pass in mandatory fields, they will be parsed and type validated. e.g if you pass in an int to str,
#    it will be converted to a str. If you pass in a str to an int, it will be converted to an int.
# 3. By default, all fields are mutable i.e. they can be changed.
# 4. Objects created from BaseModel can be converted to a dict and back again using user.dict() or dict(user).