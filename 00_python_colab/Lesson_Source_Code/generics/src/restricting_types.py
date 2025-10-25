from typing import TypeVar, cast

Numeric = TypeVar('Numeric', bound=int | float)  # Only int or float

def add(a: Numeric, b: Numeric) -> Numeric:
    return  a + b # type: ignore

x = add(5, 10)  # ✅ Valid
y = add(3.14, 2.71)  # ✅ Valid

#example of valid usage
print(type(x), x) # ✅ Valid
print(type(y), y) # ✅ Valid

#example of invalid usage
#print(add("Hello", "World"))  # ❌ Error: Argument 1 to "add" has incompatible type "str"; expected "Numeric"

#Commands to run the code:
# uv run .\restricting_types.py
# uv run mypy .\restricting_types.py