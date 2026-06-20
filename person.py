from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def show_info(self):
        pass