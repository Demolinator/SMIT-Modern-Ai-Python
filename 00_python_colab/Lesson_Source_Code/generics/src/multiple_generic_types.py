def get_value[K, V](d: dict[K, V], key: K) -> V:
    return d[key]

person = {"name": "Alice", "age": 30}
print(get_value(person, "name"))  # Returns "Alice" (str)
print(get_value(person, "age"))   # Returns 30 (int)



#Commands to run the code:
# uv run .\multiple_generic_types.py
# uv run mypy .\multiple_generic_types.py