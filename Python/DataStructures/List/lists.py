list1: list = [11,2,3,4,5,6,]


for index in range(0,len(list1),1):
    # print(index) #  print index of list start from 0 to length -1 of list
    # print(list1[index]) # print values at index

    print(f"{index} -> {list1[index]}") # print value with index


list2: list = [12, 34, 56]

for index, value in enumerate(list2):
    print(f"{index} -> {value}")


# two dimensioanl list
_2dList = [
    [0, 2],  # row 0
    []       # row 1
]

_2dList[0][0] = 1
_2dList[0][1] = 12
_2dList[1].append(12)
_2dList[1].append(24)

print(_2dList)

rows, cols = 2, 2
_2dList = [[0 for _ in range(cols)] for _ in range(rows)]
_2dList[0][0] = 1
_2dList[0][1] = 12
_2dList[1][0] = 14
print(_2dList)


def avoid_index_out_of_range(array: list) -> tuple[str]:
    if len(array) == 0:
        return "Empty List"
    
    length = len(array)

    result = []
    for index, value in enumerate(array):
        result.append(f"{index} -> {value}")
    
    return tuple(result)  # returning tuple of strings

print(avoid_index_out_of_range([1,2,3]))
result = avoid_index_out_of_range([])