# 1. Write a Python program using a for loop to print numbers from 1 to 10.
numbers = [number for number in range(1, 10 + 1)]
print(numbers)


# 2. Write a Python function using a while loop to count down from 5 to 1.
def count_numbers_from_5_to_1():
    count = 5
    while count >= 1:
        print(count)
        count -= 1


count_numbers_from_5_to_1()


# 3. Write a Python function that asks for user input until the word 'exit' is entered.
def exit_from_inputs():
    while True:
        word = input("Enter a words: ")
        if word == "exit":
            break


exit_from_inputs()


# 4. Create a Python function using a for loop and range() to print even numbers from 2 to 20.
def print_even_numbers_in_range():
    even_numbers = [number for number in range(2, 20 + 1) if number % 2 == 0]
    print(even_numbers)


print_even_numbers_in_range()


# 5. Write a program that iterates over a list of names and prints each with a serial number using enumerate().
def list_of_names(names: list):
    for index, name in enumerate(names):
        print(f"{index}) {name}")


names_lists = ["Veeresh", "Harish", "Bharath"]
list_of_names(names_lists)


# 6. Simulate a do-while loop in Python that asks for a number until the user enters a negative number.
def exit_from_function_if_enter_negative_number():
    while True:
        number = int(input("Enter a number: "))
        if number < 0:
            break


exit_from_function_if_enter_negative_number()


# 7. Create a Python program that uses a nested loop to print the multiplication table from 1 to 5.
def multiplication_table_from_1_to_5():
    for number1 in range(1, 5 + 1):
        print(f"\nMultiplication Table for {number1} \n")
        for number2 in range(1, 10 + 1):
            print(f"{number1} X {number2} = {number1*number2}")


multiplication_table_from_1_to_5()


# 8. Write a Python function that breaks the loop when the input number is divisible by 7.
def breaks_loop_input_divisisble_by_7():
    while True:
        user_input = int(input("\nEnter a Number: "))
        if user_input % 7 == 0:
            break


breaks_loop_input_divisisble_by_7()


# 9. Write a Python program using continue to skip numbers divisible by 3 from 1 to 15.
def skip_number_if_divisible_3_from_1_to_15():
    for number in range(1, 15 + 1):
        if number % 3 == 0:
            continue
        print(number)


skip_number_if_divisible_3_from_1_to_15()


# 10. Write a Python program to iterate over two lists using zip() and print the paired elements.
def zip_two_lists(list1: list, list2: list) -> list:
    paired_items = []
    for item1, item2 in zip(list1, list2):
        # print(f"paired items: ({item1},{item2})")
        paired_items.append((item1, item2))  # Append the paired elements as a tuple
    return paired_items


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [465, 6, 7, 8, 6, 3, 5]
print(zip_two_lists(list1, list2))
