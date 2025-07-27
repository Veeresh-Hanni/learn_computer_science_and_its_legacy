# 🐍 Python Basic Data Types Example

This simple Python script demonstrates **fundamental data types** used in Python with examples and type checking using the `type()` function.

---

## 📌 Code Overview

```python
# Integer
num = 10

# Float
price = 19.99

# String
name = "Alice"

# Large integer
large_num = 12345678901234567890

# Long float
long_float = 3.14159265358979323846

# Boolean
is_active = True

# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10.0, 20.0)

# Dictionary
person = {"name": "Bob", "age": 25}

# Set
unique_numbers = {1, 2, 3, 4}

# Printing types
print(type(num))              # <class 'int'>
print(type(price))            # <class 'float'>
print(type(name))             # <class 'str'>
print(type(is_active))        # <class 'bool'>
print(type(fruits))           # <class 'list'>
print(type(coordinates))      # <class 'tuple'>
print(type(person))           # <class 'dict'>
print(type(unique_numbers))   # <class 'set'> 
```


# 🐍 Python Functions Example

This repository contains a simple Python program that demonstrates:

- ✅ Function Declaration  
- ✅ Function Definition  
- ✅ Function Invocation (Calling)  
- ✅ Use of `pass`  
- ✅ Type Hinting (`-> None`)  
- ✅ Importance of Indentation in Python  

---

## 📌 Code Overview

```python
# Function declaration and definition
def enoMadabeda():
    # do nothing
    pass


def print_message() -> None:
    # Indentation is super important in Python
    # It is like curly braces in other languages
    print("Namaskara Bharath!")


# Function invocation / calling
enoMadabeda()
print_message()
```
### example 2

```python 
# Function Definition
def nanuFirstFunction() -> None:
    print("Nanu First Function")
    # Calling 2 Function inside 1 Function
    nanuSecondFunction()


def nanuSecondFunction() -> None:
    print("Nanu Second Function")
    # Calling 1 Function inside 2 Function
    nanuFirstFunction()

    """
    # Cause Error
    RecursionError: maximum recursion depth exceeded

    """


# Function Invocation
nanuFirstFunction()
```

### 
```python
# Parameterized Constructor
def print_student_details(name: str, age: int, cgpa: float) -> int:
    print("Students Details:\n")
    print("Student Name is: ", name)
    print("Student age is: ", age)
    print("Student CGPA is: ", cgpa)
    print(f"{name} is {age} years old has CGPA {cgpa}\n")

    return age, name


def print_student_details_simple(name, age, cgpa):
    print("Student Name is: ", name)
    print("Student age is: ", age)
    print("Student CGPA is: ", cgpa)

    return age, name


student_age = print_student_details("Veeresh", 19, 9.5)  # function with arguments
print("Student age returned is: ", student_age)

student_age2, student_name = print_student_details_simple(
    "Ramesh", 20, 8.7
)  # function with arguments


print(
    "Student age returned is: ",
    student_age2,
    ", ",
    "Student Name returned  is: ",
    student_name,
)
```