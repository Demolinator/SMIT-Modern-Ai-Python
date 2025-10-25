class Cache[K, V]:
    def __init__(self):
        self.store: dict[K, V] = {}
    
    def set(self, key: K, value: V) -> None:
        self.store[key] = value
    
    def get(self, key: K) -> V:
        return self.store[key]

# Usage
cache = Cache[str, int]()
cache.set("count", 10)
print(cache.get("count"))  # Output: 10

#Command to run the code:
# uv run .\caching_system.py
# uv run mypy .\caching_system.py