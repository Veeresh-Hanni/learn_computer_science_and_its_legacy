numbers = [1,4,9]

numbers.append(5)
numbers.append(11)
numbers.append(6)

print(numbers)

numbers.sort()

print(numbers)

numbers.insert(2,100)

print(numbers)

numbers.remove(11)

print(numbers)

numbers.reverse()

print(numbers)

value = numbers.pop()

print(value)

print(numbers)

for number in numbers:
    print(number)

print(numbers[3])
print(numbers[2])

matrix = [
    [1,2,3],
    [4,5,6],
    [9,98,8]
]

print(matrix)

matrix[0][0] = 100
matrix[0][1] = 200

for row in range(0,len(matrix),1):
    for col in range(0,len(matrix[row]),1):
        print(matrix[row][col],end=" ")
    print()

print(matrix)