## path parameter
To modify dynamic path we can use path function which used as parameter in path operation function.
```
@app.get('/user/{id}')
async def users(id:int):
    return id
```
we can validate or modify this id parameter using path function.
path function having some commond features:
- title 
- description
- deprecated
- alias
- For Numeric:
  - gt(greater than) , ge(greater than or equal)
  - lt (less than) , le (less than or equal)
  - ```async def users(id:Annotated[int,Path(...,ge=1,le=1000)]): ```
- For string:
  - min_length, max_length
  - regex (regular expression)
  - ```async def users(id:Annotated[str,Path(...,min_length=1,max_length=1000)]): ```
