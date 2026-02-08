from app.models.todo import Todo
from app.db.fake_db import todos, get_next_id



def create_todo(title: str, description: str | None) -> Todo:
    todo = todo(
        id=get_next_id(),
        title=title,
        description=description,
        completed=False
    )
    todos.append(todo)
    return todo


def get_all_todos() -> list[Todo]:
    return todos


def get_todo_by_id(todo_id: Todo) -> Todo | None:
    return next((t for t in todos if t.id == todo_id), None)

# next(iterator, default)

def delete_todo(todo: Todo) -> None:
    todos.remove(todo)

