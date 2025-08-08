# application.py
import re
from StudentClass import Student


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

def input_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def input_name(prompt):
    # while True:
    #     name = input_non_empty(prompt)
    #     special_chars = "!@#$%^&*()_+=><?/.,~`"
    #     if any(char.isdigit() for char in name):  # Check if any character is a digit
    #         print("Name cannot contain numbers. Please try again.")
    #     elif any(char in special_chars for char in name):  # check each char
    #         print("Name cannot contain special characters. Please try again.")
    #     else:
    #         return name

    pattern = r"^[A-Za-z ]+$"  # Only letters and spaces
    while True:
        name = input_non_empty(prompt)
        if re.match(pattern, name):
            return name
        else:
            print("Invalid name. Only letters and spaces are allowed.")



class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input_name("Enter name: ")
        age = input_positive_int("Enter age: ")
        course = input_non_empty("Enter course: ")
        hometown = input_non_empty("Enter hometown: ")

        new_student = Student(name, age, course, hometown)
        self.students.append(new_student)

        print("Student added successfully!")


    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for s in self.students:
            print(s.display_info())

    def search_student(self):
        name = input_name("Enter name to search: ").strip().lower()
        found = [s for s in self.students if s.get_name().lower() == name]
        if found:
            for s in found:
                print(s.display_info())
        else:
            print(f"No student found with name = {name}.")

    def sort_students(self):
        if not self.students:
            print("No students to sort.")
            return
        choice = input("Sort by (name/age): ").strip().lower()
        if choice == "name":
            self.students.sort(key=lambda s: s.get_name())
        elif choice == "age":
            self.students.sort(key=lambda s: s.get_age())
        else:
            print("Invalid choice!")
            return
        print("Students sorted successfully!")
        self.view_students()

    def update_student(self):
        sid = input_positive_int("Enter student ID to update: ")
        for s in self.students:
            if s.get_id() == sid:
                name = input_name("Enter new name: ")
                age = input_positive_int("Enter new age: ")
                course = input_non_empty("Enter new course: ")
                hometown = input_non_empty("Enter new hometown: ")
                s.set_name(name)
                s.set_age(age)
                s.set_course(course)
                s.set_hometown(hometown)
                print("Student updated successfully!")
                return
        print("Student not found.")

            
    def delete_student(self):
        try:
            sid = int(input("Enter student ID to delete: "))
            for s in self.students:
                if s.get_id() == sid:
                    self.students.remove(s)
                    print("Student deleted successfully!")
                    return
            print("Student not found.")
        except ValueError:
            print("Please enter a valid numeric ID.")

    def run(self):
        while True:
            print("\n--- Student Management ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Sort Students")
            print("5. Update Student")
            print("6. Delete Student")
            print("7. Exit")
            choice = input("\nEnter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.sort_students()
            elif choice == "5":
                self.update_student()
            elif choice == "6":
                self.delete_student()
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    sm = StudentManagement()
    sm.run()