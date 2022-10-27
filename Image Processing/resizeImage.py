import re
from PIL import Image


def resizeImage():
    # specify the path of the image-file which you want to blur
    imgPath = r"C:\Users\ajaya\OneDrive\Desktop\GitHub Repos\Python-Projects\Image Processing\Image Files\lion.jpg"
    img = Image.open(imgPath)

    # thumbnail method resizes the image by maintaining its aspect-ratio
    img.thumbnail((400, 400))
    img.save('resizedImg.png')


resizeImage()
