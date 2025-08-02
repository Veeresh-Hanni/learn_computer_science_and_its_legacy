# 16. Function to print unique elements in an integer array 

def print_unique_elements(array: list):
    for read_index in range(0,len(array),1):
        is_duplicate = False
        for compare_index in range(0,len(array),1):
            if read_index == compare_index:
                continue

            if array[read_index] == array[compare_index]:
                is_duplicate = True
                break

        if is_duplicate == False:

            print(array[read_index])

def invoke_print_unique_elements():
    input1 = [1,2,1,4,5]
    input2 = [1,2,3,4,5]
    print_unique_elements(input1)

# invoke_print_unique_elements()

# 17. Function to print intersection or common elements of two integer arrays 
def common_elements(array1: list, array2: list) -> list:
    # list_of_common_elements = []

    for array1_value in range(0,len(array1), 1):
        is_found = False

        for array2_value in range(0,len(array2), 1):

            if array1[array1_value] == array2[array2_value]:
                # list_of_common_elements.append(array1[array1_value])

                is_found = True

                break
        
        if is_found:
            print(array1[array1_value])

    # return list_of_common_elements

def invoke_common_elements():
    array1 =[1,2,3,4,5]
    array2 = [1,7,9,0]
    common_elements(array1,array2)
    # print(common_elements(array1,array2))

# invoke_common_elements()

# 18. Function to get count of words in string
def get_count_words(string: str) -> int:
    
    counter = 1
    
    if len(string) == 0:
        return 0
    

    for character in string:

        if character == ' 'or character == '\t' or character  == '\n':
                # counter == 0
            counter += 1
            


    return counter

def invoke_get_count_words():
    string = "Hello World"
    words_count = get_count_words(string)
    print(f"words present in {string} : {words_count}")

invoke_get_count_words()

# 19. Function to print binary values of various input like integer, char, also perform shift operations on integer
def print_binary_values_of_input(number: int):
    no_of_bits = number.bit_length()
    print(f"no of bits: {no_of_bits}")

    mask = 1

    mask = mask << no_of_bits -1

    for _ in range(no_of_bits):
        if (number & mask):
            print("1",end=" ")
        else:
            print("0",end=" ")

        mask = mask >> 1

def invoke_print_binary_values_of_input():
    print_binary_values_of_input(10)


# 20. Function to remove space from string
def remove_space(string: str) :
    output = ""

    for char in string:
        if char != ' ' and char != '\t' and char != '\n':
            output += char
    
    print(output)

remove_space("Hello World")