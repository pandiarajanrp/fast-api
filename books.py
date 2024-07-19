from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
  title: str
  category: str
  author: str


#Get Req
@app.get("/books")
async def get_all_books():
  return {"message": "Hello World!!!###"}

#Path Param
@app.get("/books/{book_id}")
async def get_book_by_id(book_id):
  return {"message": f"Getting details of Book with ID {book_id}"}

#QueryParam
@app.get("/new_books")
async def get_all_books_with_query(cateogory, author):
  return {"message": f"query param {cateogory} {author}"}

#Query and Path Param
@app.get("/books/{book_id}")
async def get_book_by_id_with_query(book_id, category, author):
  return {"message": f"Getting details of Book with ID {book_id} {category} {author}"}

#Post Request
@app.post("/books")
#async def create_new_book(new_book=Body()): # old Body approach
async def create_new_book(new_book: Book):
  return {"message": f"New Book: {new_book}"}

#Put Request
@app.put("/books/{id}")
async def update_book(id, payload=Body()):
  return {"message": f"update body: {id} = {payload}"}

#Delete Request
@app.delete("/books/{id}")
async def delete_book_by_id(id, payload=Body()):
  return {"message": f"delete body: {id} = {payload}"}