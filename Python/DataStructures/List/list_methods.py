numbers: list[int] = [1,8,5,7,96,74,47]

numbers.append(3)
numbers.append(23)


print(numbers)

numbers.sort()

print(numbers)

numbers.insert(1,34)
print(numbers)

numbers.remove(7)
print(numbers)

numbers.reverse()
print(numbers)

numbers.pop()
print(numbers)

numbers.pop()
print(numbers)

for number in numbers:
    print(number)

matrix = [
    [1,2,3],
    [34,56,78]
]
print(matrix)

matrix[0][0] = 100
matrix[0][1] = 200
print(matrix)
