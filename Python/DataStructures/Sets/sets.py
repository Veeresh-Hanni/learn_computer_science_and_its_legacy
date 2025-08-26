student_ids = {100,200,101, 201, 301}
print(student_ids)

for num in range( 300):
    if num in student_ids:
        print("found")
        break
    else:
        print("not found")
        break

enrolled_students = {s.lower() for s in {"Veeresh","veeresh", "basu","sachin", "guru", "siddu","siddu"}
}
print(enrolled_students)

def find_student(name: str) -> str:

    # for student in enrolled_students:
    #     if student.lower() == name:
    #         print(f"{name} was enrolled")
    #         return
    #     else:
    #         print(f"{name} not enrolled")
            
    
    if name.lower() in enrolled_students:
            print(f"{name} was enrolled")
            
    else:
        print(f"{name} not enrolled")
        
find_student("Siddu")