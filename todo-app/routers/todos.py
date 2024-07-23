from fastapi import APIRouter, Depends, HTTPException
from models import Todos
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from routers import auth

router = APIRouter()

class TodoRequest(BaseModel):
  title: str
  description: str
  priority: str
  complete: bool

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/todos")
def get_todos(db: db_dependency):
  return db.query(Todos).all()

@router.get("/todos/{id}")
def get_todo_by_id(db: db_dependency, id: int):
  todo_result = db.query(Todos).filter(Todos.id == id).first()
  if not todo_result:
    raise HTTPException(status_code=404, detail="Todo not found")
  return todo_result

@router.post("/todos")
def create_new_todo(db: db_dependency, payload: TodoRequest):
  todo_model = Todos(**payload.dict())
  db.add(todo_model)
  db.commit()

# @router.put("/todos/{id}")
# def update_todo_by_id(db: db_dependency, id: int):


@router.delete("/todos/{id}")
def delete_todo_by_id(db: db_dependency, id: int):
  todo_model =  db.query(Todos).filter(Todos.id == id).first()
  if not todo_model:
    raise HTTPException(status_code=404, detail="Todo not found")
  db.query(Todos).filter(Todos.id == id).delete()
  db.commit()