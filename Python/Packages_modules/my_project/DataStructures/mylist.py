# mylist.py
class MyList:

    def __init__(self):
        self.list = []

    def addElements(self, item):
        self.list.append(item)

    def printList(self):
        print(self.list)

    def removeElemnt(self, item):
        self.list.remove(item)


class StudentList(MyList):
    pass
