from app.models.todo import Todo

todos: list[Todo] = []
_current_id = 1


def get_next_id() -> int:
    global _current_id
    todo_id = _current_id
    _current_id += 1
    return todo_id