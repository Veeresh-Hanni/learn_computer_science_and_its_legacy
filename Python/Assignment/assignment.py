# Python Coding Practice Questions

# 1. Write a function that adds two numbers and returns the result.
# Ans


def get_sum_of_two_numbers(number1: int, number2: int) -> int:
    result = number1 + number2
    return result


# 2. Create a function that subtracts the second argument from the first and returns the difference.

# 	Ans


def subtract_two_numbers(number1: int, number2: int) -> int:
    difference = number2 - number1
    return difference


# 3. Write a Python function to multiply two integers.
#      Ans
def multiple_two_numbers(number1: int, number2: int) -> int:
    result = number1 * number2
    return result


# 4. Create a function that divides two float numbers and returns the result.
# ANS


def divide_two_numbers(number1: float, number2: float) -> float:
    result = number1 / number2
    return result


# 5. Write a function that returns the modulus of two input integers.
# ans


def find_modules_of_two_numbers(number1: int, number2: int) -> int:
    modules = number1 % number2
    return modules


# 6. Write a function to compute the average of four numbers using arithmetic operators.
# Ans
def average_of_four_numbers(
    number1: int, number2: int, number3: int, number4: int
) -> int:
    sum = number1 + number2 + number3 + number4
    average = sum / 4
    return average


# 7. Create a function that returns both the sum and product of two numbers.
# Ans
def find_sum_and_product_of_two_numbers(number1: int, number2: int) -> tuple[int, int]:
    sum = number1 + number2
    product = number1 * number2
    return sum, product


# 8. Write a function to calculate area of a triangle given base and height using `*` and `/`.
def find_area_of_triangle(base: int, height: int) -> int:
    # formula -> Area = 1/2 * base * height
    area_of_triangle = 1 / 2 * base * height
    return area_of_triangle


# 9. Create a program to check whether a given number is even or odd using `%` operator.
def find_even_or_odd(number: int) -> int:
    is_even = False

    if number % 2 == 0:
        is_even = True
    else:
        is_even = False

    return is_even


# 10. Write a function that swaps two numbers using only arithmetic operators.
def swap_two_numbers(number1: int, number2: int) -> int:
    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2
    return number1, number2


# Call All Functions with required arguments
sum_of_two_numbers = get_sum_of_two_numbers(4, 8)
print(f"Sum of two numbers 4 + 8 = {sum_of_two_numbers} ")
difference = subtract_two_numbers(5, 4)
print(f"Subtract of two nubers 4 - 5 = {difference}")
product = multiple_two_numbers(5, 6)
print(f"Multipliaction of two numbers 5 * 6 = {product}")
quotient = divide_two_numbers(4.5, 2.4)
print(f"divident of two numbers 4.5 / 2.4 = {quotient}")
modules = find_modules_of_two_numbers(5, 2)
print(f"remainder of 5 % 2 = {modules}")
average = average_of_four_numbers(4, 5, 6, 7)
print(f"Average of (4,5,6,7) = {average}")
sum, product = find_sum_and_product_of_two_numbers(3, 5)
print(f"Sum and product of two numbers = {sum,product}")
area_of_triangle = find_area_of_triangle(5, 7)
print(f"Area of Triangle with base 5 and height 7 = {area_of_triangle}")
even_or_odd = find_even_or_odd(5)
print(f"is 5 Even? = {even_or_odd}")
swap = swap_two_numbers(4, 5)
print(f"Swap two numbers 4,5 = {swap}")
