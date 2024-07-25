from fastapi import APIRouter, Depends
from pydantic import BaseModel
from utils import db_dependency
from models import Users
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from jose import jwt
from datetime import datetime,timezone, timedelta

SECRET_KEY="5bc0bbad167b20965aef2dd72546e9e1534c97d5704d258fbec1b54a1f1fee9a"
ALGORITHM="HS256"

class CreateUserRequest(BaseModel):
  username: str
  email: str
  first_name: str
  last_name: str
  password: str
  role: str

router = APIRouter(
  prefix="/users",
  tags=["Users"]
)

def authenticate_user(username, password, db):
  user = db.query(Users).filter(Users.username == username).first()
  if not user or not user.password == password:
    return False
  else:
    return user
  
def create_access_token(username, user_id, exp):
  expires = datetime.now(timezone.utc) + exp
  encode = { 'sub': username, 'id': user_id, 'exp': expires }
  return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)



@router.post("/")
async def create_user(db: db_dependency, payload: CreateUserRequest):
  user_model = Users(**payload.model_dump())
  db.add(user_model)
  db.commit()
  return user_model

@router.post("/auth")
async def get_auth_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
  ):
  user = authenticate_user(form_data.username, form_data.password, db)
  token = create_access_token(user.username, user.id, timedelta(minutes=20))
  
  return {
    'token': token
  }