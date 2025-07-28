# Python – 5 Recursion Questions
# 1. Print numbers from 1 to N using recursion.


def print_numbers_from_1_to_n_using_recursion(n: int):
    if n <= 0:
        return 1

    print_numbers_from_1_to_n_using_recursion(n - 1)
    print(n)


print_numbers_from_1_to_n_using_recursion(9)


# 2. Calculate the sum of first N natural numbers using recursion.


def sum_of_n_natural_numbers_using_recursion(n: int) -> int:
    if n <= 1:
        return 1

    sum = sum_of_n_natural_numbers_using_recursion(n - 1)
    sum = sum + n
    return sum


print(sum_of_n_natural_numbers_using_recursion(10))


# 3. Find the factorial of a number using recursion.
def find_factorial(number: int) -> int:
    if number <= 0:
        return 1
    return number * find_factorial(number - 1)


print(find_factorial(5))


# 4. Reverse a string using recursion.
def reverse_string_using_recursion(string: str) -> str:
    if string == "":
        return ""
    return reverse_string_using_recursion(string[1:]) + string[0]


print(reverse_string_using_recursion("veeresh"))  # Output: hserreev


# 5. Check if a number is a power of 2 using recursion.
def find_power_of_2(number: int) -> bool:
    if number == 1:
        return True
    if number <= 0 or number % 2 != 0:
        return False
    return find_power_of_2(number // 2)


print(find_power_of_2(3))  # Output: False
print(find_power_of_2(8))  # Output: True
