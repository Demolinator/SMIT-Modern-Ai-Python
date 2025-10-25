class APIResponse[T, U]:
    def __init__(self, data: T, status: U):
        self.data = data
        self.status = status

# Usage
response = APIResponse[str, int]("Success!", 200)
print(response.data)  # Output: "Success!"

response2 = APIResponse[bool, float](True, 0.200)
print(response2.data)  # Output: "Success!"

#Command to run the code:
# uv run .\api_response_wrapper.py
# uv run mypy .\api_response_wrapper.py
 