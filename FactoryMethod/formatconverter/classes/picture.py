from abc import ABC, abstractmethod

class Picture(ABC): 
    def __init__(self,format):
        self.format = format

    @abstractmethod
    def converter(self):
        pass
