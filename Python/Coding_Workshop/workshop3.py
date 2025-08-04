# 11. Function to find given string is palindrome

def is_palindrome(string: str) -> bool:
    if string[::-1] == string:
        return True
    else:
        return False
        

def is_palindrome_v2(string: str) -> bool:
    result = True
    for character in range(0,len(string),1):
        for reverseCharacter in range(len(string)-1,-1,-1):
            if string[character] != string[reverseCharacter]:
                result = False
            else:
                result = True
                break
    return result



def is_palindrome_v3(string: str) -> bool:
    leftIndex = 0
    rightIndex = len(string) - 1

    result: bool = True

    while (leftIndex < rightIndex):

        if string[leftIndex] != string[rightIndex]:
            result = False
            break

        leftIndex += 1
        rightIndex -= 1

    return result

def invoke_is_palindrome():
    input1 = "madam"
    input2 = "malayalam"
    input3 = "hello"
    input4 = "abba"
    input5 = "abcedcba"

    result = is_palindrome_v3(input5)

    if(result):
        print(f"string is Palindrome")
    else:
        print(f"string is not palindrome")

    string = "abc"

    palindrome = is_palindrome_v2(string)
    print(palindrome)
    string = "a"

    is_palindrome = is_palindrome_v3(string)
    print(is_palindrome)

invoke_is_palindrome()


# 12. Function to find minimum and maximum value in array
def get_max_min_value(array: list) -> tuple[int,int]:

    max = array[0]
    min = array[0]

    for value in range(1,len(array),1):
        if array[value] > max:
            max = array[value]
        if array[value] < min:
            min = array[value]
    
    return max,min

def invoke_get_max_min_value():
    array = [34,56,78,38,0]
    max_value, min_value = get_max_min_value(array)
    print(f"{max_value} is maximum value in {array}")
    print(f"{min_value} is minimum value in {array}")


# 13. Function to search in sorted  array
# Binary Search (Divide and conquere Algorithm)
def search_key(numbers: list, key: int) -> bool:

    leftIndex = 0
    rightIndex = len(numbers)-1
    found = False

    while(leftIndex <= rightIndex):

        middleIndex = int(leftIndex + (rightIndex - leftIndex)/2) #type casting

        if (numbers[middleIndex] == key):
            found = True
            break

        if numbers[middleIndex] > key:
            # you must search on the left side of the array
            rightIndex = middleIndex - 1
        else:
            # you must search on rifht side of array
            leftIndex = middleIndex + 1
    

    return found

def invoke_search_key():
    array = [1,2,3,4,5,6]
    key = 6

    result = search_key(array, key)

    if(result):
        print("Number is found")
    else:
        print("Number is not found")

invoke_search_key()