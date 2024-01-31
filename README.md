# FastAPI_Course
- **path operation decorator** (like @app.get("/"))
- **path operation function**  (like def root(): ... above)
### Path Parameter
To generate dynamic url we simply put the parameter name in the path around curly braces.then, we define the same parameter as an argument in path operation function.
such as dynamic url : http://127.0.0.1:5000/user/{id}, here we can dynamically set id value. 
In path function let, *users* we need to define *id* as parameter. 
```
from fastapi import FastAPI
app = FastAPI()
@app.get('/user/{id}')
async def users(id):
    return {"user id":id}
```
In this example id can be string ,integer or other type.
We can define parameter type by,
```
from fastapi import FastAPI
app = FastAPI()
@app.get('/user/{id}')
async def users(id:int):
    return {"user id":id}
```
id value will be integer anything will give **422 Unprocessable Entity** validation error. To pass string ,we can define id parameter as string also. 
To narrow down our validation we can use path function for more advance.
```
from fastapi import FastAPI, status ,Path ,Query,Body 
from typing import Annotated 
app = FastAPI()
@app.get('/user/{id}')
async def users(id:Annotated[int,Path(...)]):
    return {"user id":id}
```
**path operation**
- For Numeric:
  - gt(greater than) , ge(greater than or equal)
  - lt (less than) , le (less than or equal)
  - ```async def users(id:Annotated[int,Path(...,ge=1,le=1000)]): ```
- For string:
  - min_length, max_length
  - regex (regular expression)
  - ```async def users(id:Annotated[str,Path(...,min_length=1,max_length=1000)]): ```
