def swap[T](a: T, b: T) -> tuple[T, T]:
    return b, a

x, y = swap(10, 20)    # ✅ (int, int)
a, b = swap("A", "B")  # ✅ (str, str)

print(x, y)  # Output: 20 10
print(a, b)  # Output: B A