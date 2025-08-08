# StudentClass.py


class Student:

    count = 0

    def __init__(self, name=None,age = None,course = None, hometown=None):

        self.Name = name
        self.Age = age
        self.__Course = course
        self.__ID = None
        self._Hometown = hometown

        if name and age and course and hometown:
            self.__register()

    def get_name(self):
        return self.Name
    
    def get_age(self):
        return self.Age
    
    def get_course(self):
        return self.__Course
    
    def get_ID(self):
        return self.__ID
    
    def get_hometown(self):
        return self._Hometown
    
    # private method (call inside class only, not from outer side)
    def __register(self):
        Student.count += 1
        self.__ID = Student.count
        return self.__ID
