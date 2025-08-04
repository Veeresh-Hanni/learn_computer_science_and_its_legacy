# 1. Function to get sum of two numbers
def get_sum(number1: int, number2: int) -> int:
    sum = number1 + number2
    return sum


# Immutable - int, float, string, tuple
# you can't update their values. Every time you update, new space is allocated
# 2. Function swapNumbers to swap two variable values
def swap_two_numbers(item1: int, item2: int):

    temp = item1
    item1 = item2
    item2 = temp

    return item1, item2


def swap_two_numbers_v2(item1: int, item2: int):
    return item2, item1


# 3. Function to find even Nimber
def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

# 4. Function is_number return True if it is Integer
def is_number(string: str) -> bool:
    is_num = True
    for character in string:
        if (character >= '0' and character <= '9'):
            continue
        else:
            is_num = False
            break
    return is_num


def is_number_v2(string: str) -> bool:
    for character in string:
        if (character < '0' or character > '9'):
            return False
        
    return True


# 5. Function to simple greetings
def simple_greetings(name: str) -> str:
    return (f"Namaskara, {name}")


def simple_greetings_v2() -> str:
    name = input("Enter Your Name: ")
    age =(input("Enter your age: "))
    print(f"Namaskara, {name} you're {age} year's now")



# Invoction
def invoke_get_sum():
    sum = get_sum(5, 7)
    print(
        f"Sum of Two numbers is: {sum}"
    )  # Polymorphism Concepts same function but diffrentdtatype arguments

    sum1 = get_sum(2.3, 4.5)
    print(f"Sum of Two numbers is: {sum1}")

    sum2 = get_sum("Hello ", "World!")
    print(f"Sum of Two numbers is: {sum2}")


def invoke_swap_functions():
    number1 = 10
    number2 = 20

    print(f"Before swap: value of number1 = {number1} and number2 = {number2}")

    number1, number2 = swap_two_numbers(number1, number2)
    number1, number2 = swap_two_numbers_v2(number1, number2)

    print(f"After swap: value of number1 = {number1} and number2 = {number2}")


def invoke_is_even():

    input = 100
    result = is_even(input)
    if result:
        print(f"{input} is Even")
    else:
        print(f"{input} is Odd")

def invoke_is_number_v1_v2():

    input = "asdfreccvf"
    string = is_number_v2(input)
    # print(string)

    if string:
        print(f"{input} is Integer")


invoke_get_sum()
invoke_swap_functions()
invoke_is_even()

invoke_is_number_v1_v2()

simple_greetings_v2()