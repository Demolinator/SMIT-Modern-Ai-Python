from fastapi import APIRouter, HTTPException, status
from app.schemas.todo import TodoResponse, TodoCreate
from app.services import todo_service


router = APIRouter(tags=["Todos"])

    # {
    #     title: "Go to Work",
    #     description: "I love to go to work."
    # }

@router.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    return todo_service.create_todo(todo.title, todo.description)


@router.get("/todos", response_model=list[TodoResponse])
def get_todos():
    return todo_service.get_all_todos()


@router.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int):
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    return todo


@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    todo_service.delete_todo(todo)

