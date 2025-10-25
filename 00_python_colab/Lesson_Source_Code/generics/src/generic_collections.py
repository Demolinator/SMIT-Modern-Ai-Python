names: list[str] = ["Alice", "Bob"]
ages: dict[str, int] = {"Alice": 25, "Bob": 30}
unique: set[int] = {1, 2, 3}

 
print(names)  # Output: ['Alice', 'Bob']
print(ages)   # Output: {'Alice': 25, 'Bob': 30}   
print(unique)  # Output: {1, 2, 3}

#uncommenting the following line will cause a type error
#names.append(35)  # Adding an integer to a list of strings


#Commands to run the code:
# uv run .\generic_collections.py
# uv run mypy .\generic_collections.py