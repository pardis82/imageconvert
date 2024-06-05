from abc import ABC, abstractmethod

class Picture(ABC): 
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def area(self):
        pass
