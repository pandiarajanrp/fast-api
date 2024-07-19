from fastapi import FastAPI

app = FastAPI()

#Get Req
@app.get("/books")
async def get_all_books():
  return {"message": "Hello World!!!###"}

#Path Param
@app.get("/books/{book_id}")
async def get_all_books(book_id):
  return {"message": f"Getting details of Book with ID {book_id}"}