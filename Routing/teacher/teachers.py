from fastapi import APIRouter, Path ,Query
from typing import Annotated
router = APIRouter()

@router.get('/teacher/names')
async def teacher_name(name:Annotated[str,Query(...)]):
    return {"teacher name ":name}

@router.get('/teacher/{id}')
async def teacher_id(id:Annotated[int,Path(...)]):
    return {"teacher id ":id}

