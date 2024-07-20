from pydantic import BaseModel, Field
from typing import Optional

class Posts:
  id: int
  title: str
  content: str
  author: str
  rating: float

  def __init__(self, id, title, content, author, rating):
    self.id = id
    self.title = title
    self.content = content
    self.author = author
    self.rating = rating

class PostRequest(BaseModel):
  id: Optional[int] = None
  title: str = Field(min_length=3)
  content: str = Field(min_length=10)
  author: str = Field(min_length=4)
  rating: float = Field(gt=0, lt=6)

  model_config = {
    "json_schema_extra": {
      "example": {
        "title": "Basics of Js",
        "content": "Learn the basics of JS",
        "author": "RP",
        "rating": 5
      }
    }
  }

POSTS = [
  Posts(1, "Importance of Basic", "Importance of basics in Software Development", "PR", 4),
  Posts(2, "Kubernetes Basics", "Kubernetes Basics in containersation", "PR", 3.5),
  Posts(3, "Python Advanced", "Python Advanced in Software Development", "PR", 3.6)
]

