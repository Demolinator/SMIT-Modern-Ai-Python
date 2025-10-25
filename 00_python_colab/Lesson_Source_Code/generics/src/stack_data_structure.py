class Stack[T]:
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Usage
int_stack = Stack[int]()
int_stack.push(10)
print(int_stack.pop())  # ✅ Returns int

str_stack = Stack[str]()
str_stack.push("hello")
print(str_stack.pop())  # ✅ Returns str

# Uncommenting the following lines will cause type errors
#int_stack.push("world")  # ❌ Type error: Argument 1 to "push" of "Stack" must be "int"
#str_stack.push(20)  # ❌ Type error: Argument 1 to "push" of "Stack" must be "str"

#Commands to run the code:
# uv run .\stack_data_structure.py
# uv run mypy .\stack_data_structure.py