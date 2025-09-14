student_list_empty = {'name':''}

student_list_empty[1] = "Ids"
student_list_empty['name'] = "Veeresh"
student_list_empty['name'] = "Guru"

student_list = {"123": "Guru"}

print(student_list_empty)
print(student_list)

name = student_list.get('123')
print(f"Name of student: {name}")
print(student_list_empty.keys())
print(student_list_empty.values())
print(student_list_empty.items())
print(student_list_empty.pop(1))
print(student_list_empty.clear())