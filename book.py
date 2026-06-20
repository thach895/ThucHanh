from abc import ABC, abstractmethod

class Displayable(ABC):

    @abstractmethod
    def show_info(self):
        pass


class Book(Displayable):
    def __init__(self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def borrow_book(self):
        if self.__quantity <= 0:
            raise ValueError("Book is out of stock!")
        self.__quantity -= 1

    def return_book(self):
        self.__quantity += 1

    def show_info(self):
        print(
            f"{self.id} | {self.title} | {self.author} | {self.__quantity}"
        )