class Todo:
    def __init__(self, id: int, title: str, description: str | None, completed: bool):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed