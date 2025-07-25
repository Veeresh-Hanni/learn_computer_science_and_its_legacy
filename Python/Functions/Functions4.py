# Parameterized Constructor
def print_student_details(name: str, age: int, cgpa: float) -> int:
    print("Students Details:\n")
    print("Student Name is: ", name)
    print("Student age is: ", age)
    print("Student CGPA is: ", cgpa)
    print(f"{name} is {age} years old has CGPA {cgpa}\n")

    return age, name


def print_student_details_simple(name, age, cgpa):
    print("Student Name is: ", name)
    print("Student age is: ", age)
    print("Student CGPA is: ", cgpa)

    return age, name


student_age = print_student_details("Veeresh", 19, 9.5)  # function with arguments
print("Student age returned is: ", student_age)

student_age2, student_name = print_student_details_simple(
    "Ramesh", 20, 8.7
)  # function with arguments


print(
    "Student age returned is: ",
    student_age2,
    ", ",
    "Student Name returned  is: ",
    student_name,
)
