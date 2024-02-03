from fastapi import FastAPI, Path , status
from typing import Annotated 
app = FastAPI()

@app.get('/user/{id}',status_code=status.HTTP_200_OK)
async def users(id:Annotated[int,Path(title="user id",ge=0,le=1000)]): #user id is integer which validated by 1 <= id <= 1000
    return {"user id":id}

@app.get('/user_name/{name}',status_code=status.HTTP_200_OK) #user name is string which validated by max_length==3 and min_length==100
async def users(name:Annotated[str,Path(title="user name",min_length=0,max_length=100)]):
    return {"user name":name}

#path parameter should be named as decorator function's dynamic parameter.
#if use alais then alais name and  decorator function's dynamic parameter must be same.
@app.get('/user_address/{address}',status_code=status.HTTP_200_OK) #user address is string which validated by max_length==3 and min_length==1000
async def users(addr:Annotated[str,Path(title="user address",min_length=0,max_length=1000 ,alias="address")]):
    return {"Address ":addr}


@app.get('/user_contact/{contact}',status_code=status.HTTP_200_OK) #user contact is string which validated by max_length==3 and min_length==11
async def users(contact:Annotated[str,Path(title="user contact",min_length=0,max_length=11 ,alias="contact" ,description="Here is User contact")]):
    return {"Contact ":contact}

@app.get('/user_contact/{info}',status_code=status.HTTP_200_OK) #user contact is string which validated by max_length==3 and min_length==11
async def users(info:Annotated[str,Path(title="user info",min_length=0,max_length=10 ,alias="info" ,description="Input User information",deprecated=True)]):
    return {"Contact ":info}

from enum import Enum
class enum_type(str,Enum):
    food = "vagitable"
    meat = "beef"

@app.get('/user_eat/{typ}')
async def eats(eat:Annotated[enum_type,Path(...)]):
    return eat


