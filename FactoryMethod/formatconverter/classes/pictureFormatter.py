
from FactoryMethod.formatconverter.classes.gif import Gif
from FactoryMethod.formatconverter.classes.jpeg import Jpeg
from FactoryMethod.formatconverter.classes.png import Png


class PictureFormatter:
    def create_picture(self,format,*args):
        self.picture_classes = {
            "Jpeg": Jpeg,
            "Png": Png,
            "Gif": Gif
        }
        picture_class = self.picture_classes.get(format)
        return picture_class(format,*args)
