from fastapi import FastAPI, status ,Path ,Query,Body 
from typing import Annotated
app = FastAPI()

#path parameter should be named as decorator function's dynamic paramer.
#if use alais then alais name and  decorator function's dynamic paramer must be same.

@app.get('/user/{id}',status_code=status.HTTP_200_OK)
async def users(id:Annotated[int,Path(title="user id",ge=1,le=20,alias='user-id')]):
    return id

@app.get('/users/{name}',status_code=status.HTTP_200_OK)
async def users_name(id_:Annotated[str,Path(title="user name",min_length=3,max_length=20,alias='name')]):
    return id_
