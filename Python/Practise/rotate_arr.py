def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end],arr[start]
        start += 1
        end -= 1


def rotate_arr(arr: list[int], do: int):
    n = len(arr)
    
    if do == n:
        return arr
    
    do %= n

    reverse(arr, 0, do - 1)

    reverse(arr, do, n - 1)

    reverse(arr, 0, n - 1)
    
    return arr

print(rotate_arr([1,2,3,4,5], 5))