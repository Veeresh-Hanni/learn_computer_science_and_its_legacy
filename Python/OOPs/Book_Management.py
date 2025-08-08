# Book_Management.py 

class BookManagement:


    def check_out(self, student, book):
        print(f"Student {student.Name} is taking book {book.get_title()}")
        return True
    
    def return_book(self, student, book):
        print(f"Student {student.Name} is returning book {book.get_title()}")