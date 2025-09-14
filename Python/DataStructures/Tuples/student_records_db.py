
student_db = []

def add_student():

    id = int(input("Enter the id: "))

    name = input("Enter the name: ")

    student_records = (id, name)

    student_db.append(student_records)

def print_all():
    if not student_db:
        print("Empty Records")
    
    for student_rec in student_db:
        print(f"Id: {student_rec[0]}, Name: {student_rec[1]}")
        print(student_rec)

def search(name):
    
    if not student_db:
        print("No Records found")
        return
    
    for std_rec in student_db:
        student_id = std_rec[0]   # assuming 0th index = ID
        student_name = std_rec[1] # assuming 1st index = Name
        if name.isdigit() and int(name) == student_id:
            print(f"{name} found in Records")
            return
        elif name == student_name:
            print(f"{name} found in Records")
            return
        
    print(f"{name} not found in Records")


if __name__ =="__main__":
    add_student()
    # add_student()
    print_all()
    name = input("Enter a Name or id: ")
    search(name)
    print_all()