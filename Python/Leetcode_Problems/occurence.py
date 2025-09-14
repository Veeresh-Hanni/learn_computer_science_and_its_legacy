def find_first_dupliactes(list1: list):
    seen = {}
    for num in list1:
        if num not in seen:
            seen[num] = 1
        elif num in seen:
            seen[num] += 1
            print(num)
            print(seen)
            return
    


    # for num in range(1, len(list1), 1):
    #     for num2 in range(num+1, len(list1), 1):
    #         if (list1[num] == list1[num2]):
    #             print(list1[num])
    #             return
    # print("None")


def find_first_occurence(numbers: list, target: int)-> int:
    if target not in numbers:
            print(f"{target} Not in List")
            return
    
    for index, num in enumerate(numbers, start=1):
        if num == target:
            break

    print(f"{num} number at Position: {index}")

list = [1,2,3,6,6,5,5,4]
find_first_dupliactes(list)

find_first_occurence(list, 6)