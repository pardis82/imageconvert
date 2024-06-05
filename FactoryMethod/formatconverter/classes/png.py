from .picture import Picture

class Png(Picture):
    def __init__(self,toformat,fromformat):
        super().__init__(format)
        self.fromformat = fromformat
        self.toformat = toformat

    def converter(self):
        return self.fromformat + " converted to "+ self.toformat    + " successfully" 
   

   
   
   