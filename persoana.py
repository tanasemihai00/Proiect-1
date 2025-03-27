from abc import ABC, abstractmethod

class Persoana(ABC):
    def __init__(self, id, nume):
        self.id = id
        self.nume = nume

    @abstractmethod
    def __str__(self):
        pass
