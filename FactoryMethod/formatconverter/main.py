
from FactoryMethod.formatconverter.classes.pictureFormatter import PictureFormatter

def calculate_picture_format(format,*args):
    factory = PictureFormatter()
    picture = factory.create_picture(format,*args)
    return picture.converter()

pic_format = calculate_picture_format('Gif','Png')
pic2_format = calculate_picture_format('Jpeg','Png')
print(pic_format)
print(pic2_format)

