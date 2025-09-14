# class Find_Duplicates:
def find_duplicates(arr: list) -> list:
    counter = {}

    for val in arr:
        if val not in counter:
            counter[val] = 1
        else:
            counter[val] += 1
        
        # or using dict methods
        # counter[val] = counter.get(val, 0) + 1
        
    # List comprehension to return values which has > 1
    # return [val for val in counter if counter[val] > 1]
    return [{key:val} for key ,val in counter.items() if val > 1]

print(find_duplicates([1,2,3,4,4,5,6,5]))  #empty array

def find_duplicates_v2_count(arr: list) -> list:
    # dub_val = []
    # for val in arr:
    #     if arr.count(val) > 1 :
    #         dub_val.append(val)
    # return list(set(dub_val))

    dub_val = []
    for val in arr:
        if arr.count(val) > 1 and val not in dub_val:
            dub_val.append(val)
    return dub_val


print(find_duplicates_v2_count([1,2,3,4,456,4,4,4,5,5]))

def find_duplicates_v2_sets(arr: list) -> list:
    seen = set()
    dub = set()

    for val in arr:
        if val not in seen:
            seen.add(val)
        else:
            dub.add(val)
    
    return list(dub)

print(find_duplicates_v2_sets([1,2,3,4,5,6,6,7,7,8]))


def find_duplicates_in_memory(arr: list) -> list:

    start = 0
    end = start + 1

    while (start == end) :

        if arr[start] != arr[end]:
            continue
            
        start += 1
        end += 1

    return arr

print(find_duplicates_in_memory([1,2,3,4, 4]))