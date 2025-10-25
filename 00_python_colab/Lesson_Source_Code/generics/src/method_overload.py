from typing import overload

@overload
def double(x: int) -> int: ...
@overload
def double(x: str) -> str: ...

# uncommenting the following line will cause a error
# i: int = 5 # Nothings comes in between ovrload signature and implementation 
# error: An overloaded function outside a stub file must have an implementation  [no-overload-impl]

def double(x: int | str) -> int | str:
    return x * 2

print(double(5))     # Returns 10 (int)
print(double("A"))   # Returns "AA" (str)


# Uncommenting the following lines will cause type errors
#print(double(5.0))  # ❌ Type error: Argument 1 to "double" has incompatible type "float"; expected "int | str"


#Commands to run the code:
# uv run .\method_overload.py
# uv run mypy .\method_overload.py