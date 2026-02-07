from pydantic import BaseModel
from typing import Optional


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool

# {
#     id: 1
#     title: "Go Shopping",
#     description: "I love Shopping",
#     completed: False
# }

# database