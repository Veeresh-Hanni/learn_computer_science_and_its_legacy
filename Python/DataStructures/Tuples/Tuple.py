a = tuple(i  for i in range(1,10+1))
for num in a:
    print(num, end=" ")
print()
print(a)

one_tuples = (10,)
multi_tuple = 10,2,2

print(type(one_tuples))
print(type(multi_tuple))

student = ("Veeresh", "SDE","Ful stack","Python", 19, 60.7)
print(len(student)-1)  # 5
index = 0
try:
    # print(student[0])
    # print(student[1])
    # print(student[2])
    # print(student[3])
    # print(student[4])
    # print(student[5])
    while index < len(student):
        print(student[index])
        index += 1
    
except IndexError:
    print("Index out of range")