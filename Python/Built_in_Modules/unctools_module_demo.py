from functools import (
    reduce, partial, lru_cache, wraps, cmp_to_key, total_ordering, cache
)

# 1️⃣ reduce() → Applies a function cumulatively to items of a sequence
print("1️⃣ reduce() Example:")

from operator import add, mul
nums = [1, 2, 3, 4]

sum_all = reduce(add, nums)           # 1 + 2 + 3 + 4 = 10
product_all = reduce(mul, nums)       # 1 * 2 * 3 * 4 = 24

print("Sum:", sum_all)
print("Product:", product_all)
print("-" * 40)


# 2️⃣ partial() → Fix some arguments of a function and create a new function
print("2️⃣ partial() Example:")

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print("5 squared =", square(5))
print("3 cubed =", cube(3))
print("-" * 40)


# 3️⃣ lru_cache() → Least Recently Used cache for speeding up recursive functions
print("3️⃣ lru_cache() Example:")

@lru_cache(maxsize=1000)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci(10):", fib(10))
print("Fibonacci(30):", fib(30))
print("Cache Info:", fib.cache_info())  # Shows hits, misses, etc.
print("-" * 40)


# 4️⃣ wraps() → Preserves metadata of decorated functions
print("4️⃣ wraps() Example:")

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a person"""
    return f"Hello, {name}!"

print(greet("Veeresh"))
print("Function name:", greet.__name__)   # preserved
print("Docstring:", greet.__doc__)        # preserved
print("-" * 40)


# 5️⃣ cmp_to_key() → Convert old-style comparison function to a key function (for sorting)
print("5️⃣ cmp_to_key() Example:")

def compare_length(a, b):
    return len(a) - len(b)

words = ["python", "ai", "machine", "data", "ml"]
sorted_words = sorted(words, key=cmp_to_key(compare_length))
print("Sorted by length:", sorted_words)
print("-" * 40)


# 6️⃣ total_ordering() → Fills in missing comparison methods automatically
print("6️⃣ total_ordering() Example:")

@total_ordering
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        return f"{self.name}(${self.salary})"

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1 < emp2)   # True
print(emp1 <= emp2)  # True (auto-generated)
print(emp1 >= emp2)  # False (auto-generated)
print("-" * 40)


# 7️⃣ cache() → Same as lru_cache(maxsize=None)
print("7️⃣ cache() Example:")

@cache
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print("Factorial(5):", factorial(5))
print("Factorial(10):", factorial(10))
print("-" * 40)


# 8️⃣ partialmethod() → Used inside classes (like partial, but for methods)
from functools import partialmethod

print("8️⃣ partialmethod() Example:")

class Logger:
    def log(self, level, message):
        print(f"[{level.upper()}]: {message}")

    info = partialmethod(log, "info")
    error = partialmethod(log, "error")

logger = Logger()
logger.info("System started")
logger.error("Something went wrong")
print("-" * 40)


# ✅ Summary
print("✅ functools helps with:")
print("""
- reduce(): Combine elements cumulatively
- partial(): Pre-fill some arguments
- lru_cache()/cache(): Memoize results
- wraps(): Preserve function metadata
- cmp_to_key(): Custom sorting logic
- total_ordering(): Auto-generate comparison operators
- partialmethod(): Predefined method arguments in classes
""")
