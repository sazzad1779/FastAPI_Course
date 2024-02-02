

#path parameter should be named as decorator function's dynamic paramer.
#if use alais then alais name and  decorator function's dynamic paramer must be same.

# from fastapi import FastAPI, status ,Path ,Query,Body 
# from typing import Annotated
# app = FastAPI()

# # with out function parameter id data type 
# @app.get('/user/{id}')
# async def users(id):
#     return id

# # with out function parameter id data type 
# @app.get('/user/{id}')
# async def users(id:int):
#     return id
from fastapi import FastAPI, status ,Path ,Query,Body 
from typing import Annotated
app = FastAPI()
@app.get('/user/{id}')
async def users(id:Annotated[int,Path(...)]):
    return {"user id":id}