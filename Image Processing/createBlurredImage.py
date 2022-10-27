from PIL import Image, ImageFilter


def createBlurredImage():
    # specify the path of the image-file which you want to blur
    imgPath = r"C:\Users\ajaya\OneDrive\Desktop\Python Projects\Image Processing\lion.jpg"
    img = Image.open(imgPath)
    blurredImg = img.filter(ImageFilter.BLUR)

    img.show()  # actual image
    blurredImg.show()  # blurred image


createBlurredImage()
