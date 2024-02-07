from student.students import router as student_router
from teacher.teachers import router as teacher_router
from fastapi import FastAPI
app = FastAPI()
app.include_router(student_router,tags=['student'])
app.include_router(teacher_router,tags=["teacher"])

