# LibraryItemCLass.py

from abc import ABC,abstractmethod

# Parent Class - abstract method
class LibraryItem(ABC):

    # constructor
    def __init__(self, count,id):
        self.count = count
        self.id = id
    
    def display_info(self):
        print(f"Count:{self.count}")
        print(f"id:{self.id}")
    
    @abstractmethod
    def check_out(self):
        print(f"Invoking absract method from parent class {__name__}")