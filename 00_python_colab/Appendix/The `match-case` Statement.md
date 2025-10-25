# Python `match-case` Statement – Detailed Tutorial

Python introduced the `match-case` statement in **Python 3.10** as a way to implement **structural pattern matching**, which provides a cleaner and more readable alternative to traditional `if-elif-else` chains.

---

## **1. Basic Syntax**
The `match-case` statement works by comparing an expression against multiple patterns. The syntax is:

```python
match variable:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default case (similar to "else")
```
- `variable`: The value being matched.
- `pattern1, pattern2`: Patterns to match against.
- `_`: A wildcard pattern that matches anything (acts as a default case).

---

## **2. Simple Example**
```python
def check_status(code):
    match code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case _:
            print("Unknown Status")

check_status(200)  # Output: OK
check_status(404)  # Output: Not Found
check_status(500)  # Output: Unknown Status
```

---

## **3. Matching Multiple Values**
We can match multiple values using the **`|` (OR operator)**.

```python
def is_vowel(letter):
    match letter.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            return True
        case _:
            return False

print(is_vowel('a'))  # Output: True
print(is_vowel('b'))  # Output: False
```

---

## **4. Matching Data Structures (Tuples, Lists, Dicts)**
### **Matching Tuples**
```python
def point_location(point):
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"On the X-axis at {x}")
        case (0, y):
            print(f"On the Y-axis at {y}")
        case (x, y):
            print(f"Point at ({x}, {y})")
            
point_location((0, 0))   # Output: Origin
point_location((3, 0))   # Output: On the X-axis at 3
point_location((0, 4))   # Output: On the Y-axis at 4
point_location((2, 5))   # Output: Point at (2, 5)
```

### **Matching Lists**
```python
def process_list(lst):
    match lst:
        case []:
            print("Empty list")
        case [first, second]:
            print(f"List with two elements: {first} and {second}")
        case [first, *rest]:
            print(f"First element: {first}, rest: {rest}")
        case _:
            print("Other case")

process_list([])         # Output: Empty list
process_list([1, 2])     # Output: List with two elements: 1 and 2
process_list([1, 2, 3])  # Output: First element: 1, rest: [2, 3]
```

### **Matching Dictionaries**
```python
def parse_dict(data):
    match data:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case {"name": name}:
            print(f"Name: {name}, Age not provided")
        case _:
            print("Unknown data format")

parse_dict({"name": "Alice", "age": 30})  # Output: Name: Alice, Age: 30
parse_dict({"name": "Bob"})              # Output: Name: Bob, Age not provided
parse_dict({"age": 25})                   # Output: Unknown data format
```

---

## **5. Using Guards (if Conditions in `case`)**
We can add **guards** using `if` conditions inside `case`.

```python
def check_number(num):
    match num:
        case x if x > 0:
            print("Positive number")
        case x if x < 0:
            print("Negative number")
        case 0:
            print("Zero")

check_number(10)   # Output: Positive number
check_number(-5)   # Output: Negative number
check_number(0)    # Output: Zero
```

---

## **6. Matching Class Instances**
You can match **objects** of a class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def describe(person):
    match person:
        case Person(name="Alice", age=30):
            print("Alice is 30 years old.")
        case Person(name=name, age=age) if age > 18:
            print(f"{name} is an adult.")
        case Person(name=name, age=age):
            print(f"{name} is a minor.")

p1 = Person("Alice", 30)
p2 = Person("Bob", 16)
p3 = Person("Charlie", 25)

describe(p1)  # Output: Alice is 30 years old.
describe(p2)  # Output: Bob is a minor.
describe(p3)  # Output: Charlie is an adult.
```

---

## **7. When to Use `match-case`?**
- When dealing with multiple `if-elif-else` conditions.
- When checking structured data like tuples, lists, or dictionaries.
- When working with objects and extracting attributes.

---

## **Conclusion**
The `match-case` statement is a powerful tool in Python 3.10+ that improves code readability and efficiency by allowing pattern matching. It is especially useful for working with structured data, replacing long `if-elif-else` chains.

