# Programming Paradigms in Computer Languages

## 💡 What is a *Programming Paradigm*?

A **programming paradigm** is a **way of thinking about and organizing your code**.  
It's like a **philosophy** or **style** of programming that guides how you solve problems and structure programs.

Think of it like different cuisines 🍽️:
- Italian 🇮🇹
- Chinese 🇨🇳
- Mexican 🇲🇽  
They all feed you—but with very different ingredients, techniques, and traditions. Paradigms are like that for coding.

---

## 🧱 Types of Programming Paradigms

### 1. **Imperative Programming** 🧱  
"Tell the computer exactly **how** to do something, step by step."  
You give commands, and the computer follows them in order.

🧠 **Think**: Recipe instructions 🍳  
👀 Example: C, Python (in simple scripts)

```python
x = 5
y = 10
z = x + y
print(z)
```

---

### 2. **Procedural Programming** 🔄  
A subtype of imperative programming where you **organize code into reusable procedures or functions**.

🧠 **Think**: Assembly line with stations 🛠️  
👀 Example: C, Pascal, and Python (when using lots of functions)

```python
def add(a, b):
    return a + b
```

---

### 3. **Object-Oriented Programming (OOP)** 🧸  
"Model the world as **objects** with **data** (attributes) and **behaviors** (methods)."  
Used for building big software systems.

🧠 **Think**: LEGO blocks you can combine and reuse 🧱  
👀 Example: Java, C++, Python (with classes)

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy")
my_dog.bark()
```

---

### 4. **Functional Programming** 🧼  
"Focus on **what to do**, not how. Use pure functions and avoid changing state."  
Very math-like and great for concurrency.

🧠 **Think**: Flowing water that never loops back 💧  
👀 Example: Haskell, Lisp, Scala, parts of Python

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
```

---

### 5. **Declarative Programming** 📜  
"You describe **what you want**, not how to get it."  
Let the language figure out the details.

🧠 **Think**: Ordering food at a restaurant 🍔  
👀 Example: SQL, HTML, Prolog

```sql
SELECT * FROM users WHERE age > 18;
```

---

## 🎓 Why does this matter?

- Each paradigm has **strengths and weaknesses**.
- Some languages support **multiple paradigms** (like Python, JavaScript).
- Paradigms help you **organize code better**, especially as your programs grow.

---

## ⚡ In Summary

> A **programming paradigm** is a style or way of structuring and writing code, kind of like a mindset or worldview in the coding universe.
