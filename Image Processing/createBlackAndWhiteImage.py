from PIL import Image, ImageFilter


def createBlackAndWhiteImage():
    # specify the path of the image-file which you want to blur
    imgPath = r"C:\Users\ajaya\OneDrive\Desktop\GitHub Repos\Python-Projects\Image Processing\Image Files\lion.jpg"
    img = Image.open(imgPath)

    grayImg1 = img.convert('L')
    grayImg2 = img.convert('1')

    img.show()
    grayImg1.show()
    grayImg2.show()


createBlackAndWhiteImage()
