# 14. Function to merge two arrays and return combined outputin first array

def merge_list(list1: list, list2: list) -> list:
    # list1.append(list2)
    # list1 = [item for item in list2 [list1.append(item)]]
    for item in list2:
        list1.append(item) # Heap memory allocation

def invoke_merge_list():
    list1 =  [1,2,3,4]
    list2 = [5,6,7]

    merge_list(list1,list2)

    print(list1)

# Invocation
invoke_merge_list()





# 15. Function to find second largest number
def get_second_lagest(array: list) -> int:

    first_largest = array[0]
    second_largest = array[0]

    for value in range(1,len(array),1):
        # if new number we scanned is greater than current largest
        # you have to update
        if  array[value] > first_largest:
            second_largest = first_largest
            first_largest = array[value]

        elif array[value] > second_largest or first_largest == second_largest:
            second_largest = array[value]


    return second_largest

array = [5,4,3,2,1]
result = get_second_lagest(array)
print(result)


def get_second_lagest_v2(array: list) -> int:

    largestMax = float('-inf')
    second_largest = float('-inf')


    for value in range(0,len(array),1):
        
        # if new number we scanned is greater than current largest
        # you have to update
        if  array[value] > largestMax:
            second_largest = largestMax
            largestMax = array[value]

        elif array[value] > second_largest:
            second_largest = array[value]

        # elif array[value] > second_largest or largestMax == second_largest:
        #     second_largest = array[value]

    return second_largest


import sys
def get_second_lagest_v3(array: list) -> int:

    if len(array) < 2:
        raise ValueError("Array must have at least 2 elements")

    first = second = -sys.maxsize - 1  # start with very small values

    # first = second = float('-inf')  # start with very small values

    for num in array:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
    return second

def invoke_get_second_largest():
    input1 = [-1,-2,-4,-5]
    input2 = [5,4,3,2,1]
    input3 = [1,2,3,4,5]
    input4 = [-5,-4,-3,-2,-1]
    input5 = [5,3,4,2,1]
    input6 = [-5,-2,-6]
    input7 = [-2,-6,-5]

    result = get_second_lagest_v2(input4)

    # result = get_second_lagest_v2(input7)

    # result = get_second_lagest_v3(input7)

    print(result)

invoke_get_second_largest()