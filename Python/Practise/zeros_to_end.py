from numpy import insert


def move_all_zeros_to_end(arr: list) -> list:

    # for val in range(len(arr)):
    #     for next_val in range(val+1,len(arr)):
    #         if arr[val] == 0:
    #             arr[val] = arr[next_val]
    #             arr[next_val] = 0
                
    
    # return arr
        
    insert_pos = 0  # position where next non-zero should go
    
    # Step 1: Move all non-zeros to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            # arr[insert_pos] = arr[i] # while loop
            arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
            insert_pos += 1

    # Step 2: Fill remaining positions with zeros
    # while insert_pos < len(arr):
    #     arr[insert_pos] = 0
    #     insert_pos += 1

    return arr

print(move_all_zeros_to_end(arr = [0, 0, 0,0, 0, 0]
))