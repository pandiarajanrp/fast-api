from fastapi import FastAPI, Body, Path, Query, HTTPException
from model.post import POSTS, Posts, PostRequest
from starlette import status

app = FastAPI()

@app.get("/posts")
async def get_posts(rating: int = Query(gt=0)):
  return POSTS

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(payload: PostRequest):
  #old approach with Body
  #POSTS.append(Posts(**payload["id"], payload["title"], payload["content"], payload["author"], payload["rating"]))
  #POSTS.append(Posts(**payload.dict()))
  new_book = Posts(**payload.dict())
  POSTS.append(get_post_id(new_book))
  return POSTS

@app.get("/posts/{id}")
async def get_post_by_id(id: int = Path(gt=0)):
  post = next(filter(lambda el: el.id == id, POSTS), None)
  if not post:
    raise HTTPException(status_code=404, detail='Item Not Found')
  return post

@app.put("/posts/{id}")
async def update_post_by_id(id: int, payload: PostRequest):
  post = next(filter(lambda el: el.id == id, POSTS), None)
  post = payload
  post.id = id
  print(post)
  return POSTS

@app.delete("/posts/{id}")
async def delete_post_by_id(id: int):
  result = next((item for item in list(POSTS) if item["id"] == id), None)
  print(result)

def get_post_id(post):
  post.id = 1 if len(POSTS) == 0 else POSTS[-1].id + 1
  return post