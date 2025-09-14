from xml.dom.minidom import Element


def diagonalDifference(arr):
    n = len(arr)  # number of rows (and columns since it's square)
    
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    
    for i in range(n):
        left_diagonal_sum += arr[i][i]           # top-left to bottom-right
        right_diagonal_sum += arr[i][n - i - 1]  # top-right to bottom-left
    
    return abs(left_diagonal_sum - right_diagonal_sum)

def plusMinus(arr) ->tuple[int,int,int]:
    # Write your code here
    pos = 0
    neg = 0
    zero = 0

    length = len(arr)
    for element in arr:
        if element > 0:
            pos += 1
        elif element < 0:
            neg += 1
        else:
            zero += 1
    
    # Ratios
    pos_ratio = pos / length
    neg_ratio = neg / length
    zero_ratio = zero / length

    # Print with 6 decimal places (HackerRank requirement)
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

    # Or return as tuple if you want
    return (pos_ratio, neg_ratio, zero_ratio)

arr = [1, 2, 3, -1, -2, -3, 0, 0]
result = plusMinus(arr)
print(result)