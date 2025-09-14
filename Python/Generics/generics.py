from typing import TypeVar,List

# Define a type variable that can be int or float
T = TypeVar('T', int, float)

def first_element(items: List[T]) -> T:
    print(items[0])
    return items[0]

first_element([1,2,3,4])
first_element(["a","b","6"])

def add_two_numbers(num1: T, num2: T) -> T:
    if not isinstance(num1, (int, float)):
        return (f"Invalid type for num1: {type(num1).__name__}")
    if not isinstance(num2, (int, float)):
        return (f"Invalid type for num2: {type(num2).__name__}")
    return num1 + num2

# Examples
print(add_two_numbers(5, 10))        # 15
print(add_two_numbers(3.5, 2.5))     # 6.0
print(add_two_numbers(5, 2.5))       # 7.5
print(add_two_numbers(5, "a"))       # Type Error Occurred: Maths not supported for (5, a)


