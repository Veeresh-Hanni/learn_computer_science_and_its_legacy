# student.py
class Student:
    count = 0

    def __init__(self, name, age, course, hometown):
        self.__name = name
        self.__age = None
        self.set_age(age)
        self.__course = course
        self._hometown = hometown
        self.__id = None
        self.__register()

    # ---------- Private ----------
    def __register(self):
        Student.count += 1
        self.__id = Student.count

    # ---------- Getters ----------
    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_age(self): return self.__age
    def get_course(self): return self.__course
    def get_hometown(self): return self._hometown

    # ---------- Setters ----------
    def set_name(self, name):
        if len(name.strip()) > 0:
            self.__name = name
        else:
            print("Invalid name!")

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

    def set_course(self, course):
        if len(course.strip()) > 0:
            self.__course = course
        else:
            print("Invalid course!")

    def set_hometown(self, hometown):
        self._hometown = hometown

    # ---------- Display ----------
    def display_info(self):
        return f"ID: {self.__id} | Name: {self.__name} | Age: {self.__age} | Course: {self.__course} | Hometown: {self._hometown}"
