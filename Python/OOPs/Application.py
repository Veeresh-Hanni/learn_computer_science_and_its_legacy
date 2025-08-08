# Application.py (Main File)

from StudentClass import Student
from BookClass import Book
from Book_Management import BookManagement
from MagazineClass import Magazine
from EBookClass import EBook
from OOPs.Interfaces_Abstraction.Interfaces import PaymentGateway, PayPal,BaseGateway

def main():

    new_student = Student()

    new_student.Name = "Veeresh"
    new_student.Age = 30
    new_student._Hometown = "Gadag"

    
    print(f"Student name is {new_student.get_name()}")
    print(f"Student age is {new_student.get_age()}")

    second_student = Student("Sita", 45,"Science","Bengaluru")

    print(f"Student name is {second_student.get_name()}")
    print(f"Student age is {second_student.get_age()}")

    book1 = Book("Vision to Victory","Veeresh","Life Style",1,100,123)

    # print(book.get_title())

    book1.print_book_details()
    
    book1.display_info()

    # method overloading using default argument 
    book1.search("Vision to Victory")

    # method over loading using actual argument
    book1.search("Vision to Victory", "Veeresh")

    ebook = EBook("pdf","Vision to Victory","Veeresh","Life Style",1,100,123)
    ebook.display_info()

    magazine1 = Magazine(100,123,"V","algo",100)
    magazine1.display_info()

    book_managemnt = BookManagement()

    book_managemnt.check_out(new_student,book1)
    book_managemnt.return_book(second_student,book1)

def abstract_demo():

    book1 = Book("Vision to Victory","Veeresh","Life Style",1,100,123)
    book1.check_out()

    magazine1 = Magazine(100,123, "V", "algo", 100)
    magazine1.display_info()
    magazine1.check_out()

def interfaces_demo():
    # paymnent_gw = PaymentGateway()
    # paymnent_gw.pay() # Error not directly call interface parent class

    paypal = PayPal()
    paypal.pay(1234) # Call interface child class paypal
    paypal.refund(123)

    base_gateway = BaseGateway()
    base_gateway.pay(78787)
    base_gateway.refund(1234)

if __name__ == "__main__":
    main()
    abstract_demo()
    interfaces_demo()