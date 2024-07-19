from fastapi import FastAPI

app = FastAPI()

@app.get("/books")
async def get_all_books():
  return {"message": "Hello World!!!###"}