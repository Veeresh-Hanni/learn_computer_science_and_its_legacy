# MagazineClass.py

from LibraryItemClass import LibraryItem

class Magazine(LibraryItem):

    def __init__(self, count, id,name,publisher,issue_number):
        super().__init__(count, id)

        self.name = name
        self.publisher = publisher
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number:{self.issue_number}")

    def check_out(self):
        return super().check_out()