from fastapi import FastAPI
import models
from models import Todos
from database import engine
from routers import users, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(todos.router)
