def reverseArray(arr):
    # code here
    start = 0
    end = len(arr) - 1
    while start <= end:
        arr[start],arr[end] = arr[end],arr[start]
        
        start += 1
        end -= 1
    return arr

print(reverseArray([1,2,3,4,5]))