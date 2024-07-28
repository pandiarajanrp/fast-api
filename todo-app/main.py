from fastapi import FastAPI
from .models import Base
from .routers import users, todos
from .database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(users.router)
app.include_router(todos.router)
