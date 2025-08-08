# Base class
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def show_company(self):
        print(f"Company: {self.company_name}")


# Intermediate class (inherits Company)
class Department(Company):
    def __init__(self, company_name, department_name):
        super().__init__(company_name)
        self.department_name = department_name

    def show_department(self):
        print(f"Department: {self.department_name}")


# Derived class (inherits Department)
class Employee(Department):
    def __init__(self, company_name, department_name, employee_name):
        super().__init__(company_name, department_name)
        self.employee_name = employee_name

    def show_employee(self):
        print(f"Employee: {self.employee_name}")


# Usage
emp = Employee("TechCorp", "Engineering", "Veeresh")

emp.show_company()      # From Company class
emp.show_department()   # From Department class
emp.show_employee()     # From Employee class
