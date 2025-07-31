# 6. Function to print ASCII value of string input

def print_ascii_value_of_string(string: str) -> None:
    for eachCharacter in string:
            ascii_value = ord(eachCharacter)
            print(f" {eachCharacter} ASCII value is -> {ascii_value}")


# 7. Function to get Length of String without built_in
def length_of_string(string: str) -> tuple[str,int]:
    counter = 0
    if string != None:
        for character in string:
            counter += 1
    return f"Lengnth of {string} -> {counter}"


# 8. Function to count vowels in given string
def count_vowels(string: str) -> int:
    counter = 0
    if string is not None: # if (string != None)
        for character in string:
            if (character == 'a' or
                character == 'e' or 
                character == 'i' or
                character == 'o' or 
                character == 'u' or
                character == 'A' or
                character == 'E' or
                character == 'O' or 
                character == 'U'):

                counter += 1
            
    return f"{string} has {counter} vowels"


# 9. Function to Reverse a String of given string
def reverse_string(string: str) -> str:

    # reversed = ""

    # for endcharacter in range(len(string)-1,-1,-1):
    #     reversed += string[endcharacter]

    # return reversed


    length = len(string)
    middle = int(length/2)

    # print(f"Length: {length}")
    # print(f"Middle: {middle}")


    for start in range(0,length,1):
        print(string[start], end="")

    print()    
    
    # for end in range(length-1,-1,-1):
    #     print(string[end],end="")
    

    # for start , end in zip(range(0,length,1),range(length-1,-1,-1)):
    #     print(f"Start : {string[start]} end: {string[end]}")
        # string[start] , string[end] = string[end], string[start]


    reversed_string = ""

    for end in range(length-1,-1,-1):
        reversed_string += string[end]

    return reversed_string

def reverse_a_string(string: str):
    return string[::-1]



# 10. Function to  get sum of all alements in the integer array 
def get_sum_of_all_elements(array: list[int]) -> int:

    sum = 0
    for element in array:
        sum += element  # sum = sum + element
    return sum

def get_sum_of_all_elements_v2(array: list[int]) -> int:

    # sum = "" # For stings concate
    sum = 0 # for integers
    length = len(array)
    for index in range(0,length,1):
        sum += array[index]  # sum = sum + element

    return sum








# Invocation Code

def invoke_length_of_string():
    input1 = None # Null 
    print(length_of_string(input1))

    input2 = "" # Empty String
    print(length_of_string(input2))

    input3 = "m" # Only one item
    print(length_of_string(input3))

    input4 = "Veeresh" # many items are present
    print(length_of_string(input4))

def invoke_ascii_values():
    print_ascii_value_of_string("abc")
    print_ascii_value_of_string("ABC")
    print_ascii_value_of_string("12345")

def invoke_count_vowels():
    input = "Mahesh"
    print(count_vowels(input))

def invoke_reverse_string():
    name = "abcde"
    name = reverse_string(name)
    print(name)

def invoke_get_sum_of_all_elements():
    array = [1,2,3,4,5,6]

    # sum_of_elements = get_sum_of_all_elements(array)
    names = ["Mahesh","Veeresh"]

    # sum_of_elements = get_sum_of_all_elements(array)

    sum_of_elements = get_sum_of_all_elements_v2(array)
    # sum_of_elements = get_sum_of_all_elements_v2(names)


    print(f"Sum Of elements in {array} = {sum_of_elements}")

invoke_get_sum_of_all_elements()