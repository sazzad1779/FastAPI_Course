from fastapi import APIRouter, Path ,Query
from typing import Annotated
router = APIRouter()
@router.get('/student/names')
async def student_name(name:Annotated[str,Query(...)]):
    return {"student name":name}

@router.get('/student/Address')
async def student_Address(Address:Annotated[str,Path(...)]):
    return {"student Address ":Address}

@router.get('/student/{id}')
async def student_id(id:Annotated[int,Path(...)]):
    return {"student id ":id}
