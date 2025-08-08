
# inheritance.py
# Real-world Example: Library System (Inheritance)

class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Single inheritance
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        print(f"Book - Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

# Multiple inheritance
class DigitalResource:
    def download(self):
        print(f"Downloading '{self.title}'...")

class EBook(Book, DigitalResource):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def display_info(self):
        print(f"EBook - Title: {self.title}, Author: {self.author}, Pages: {self.pages}, File Size: {self.file_size}MB")

if __name__ == "__main__":
    book = Book("The Alchemist", "Paulo Coelho", 208)
    ebook = EBook("Atomic Habits", "James Clear", 320, 5)
    book.display_info()
    ebook.display_info()
    ebook.download()
