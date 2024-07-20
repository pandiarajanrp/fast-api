from fastapi import FastAPI, Body
from model.post import POSTS, Posts, PostRequest

app = FastAPI()

@app.get("/posts")
async def get_posts():
  return POSTS

@app.post("/posts")
async def create_post(payload: PostRequest):
  #POSTS.append(Posts(**payload["id"], payload["title"], payload["content"], payload["author"], payload["rating"]))
  #POSTS.append(Posts(**payload.dict()))
  new_book = Posts(**payload.dict())
  POSTS.append(new_book)
  return POSTS