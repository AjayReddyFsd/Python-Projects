from PIL import Image, ImageFilter


def rotateImage():
    # specify the path of the image-file which you want to blur
    imgPath = r"C:\Users\ajaya\OneDrive\Desktop\GitHub Repos\Python-Projects\Image Processing\Image Files\lion.jpg"

    # sepcify here, the degree of rotation
    degreeOfRotation = 90

    img = Image.open(imgPath)
    rotatedImg = img.rotate(degreeOfRotation)

    img.show()
    rotatedImg.show()


rotateImage()
