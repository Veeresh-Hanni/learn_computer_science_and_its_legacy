# EBook.py

from BookClass import Book

class EBook(Book):

    def __init__(self,file_format, book_title, book_author, book_category, book_id, count, id):
        super().__init__(book_title, book_author, book_category, book_id, count, id)
        self.file_format = file_format

    def display_info(self):
        super().display_info()
        print(F"File Format: {self.file_format}")