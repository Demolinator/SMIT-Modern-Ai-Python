from typing import TypeVar

class Animal: ...

class Dog(Animal): ...

class Doll(): ...

A = TypeVar('A', bound=Animal)  # Must be Animal or subclass

def make_sound(animal: A) -> None:
    print("Sound!")

make_sound(Dog())  # ✅ Valid

#make_sound(Doll())  # ❌ Error: Doll is not a subclass of Animal


#Commands to run the code:
# uv run .\upper_bounds.py
# uv run mypy .\upper_bounds.py