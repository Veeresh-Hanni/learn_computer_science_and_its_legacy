from abc import ABC, abstractmethod

class Book(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Books(Book):
    def start(self):
        print("Start..")

    def stop(self):
        print("Stop..")
        exit()

# Creating object
book = Books()
book.start()  # Call the method
book.stop()
