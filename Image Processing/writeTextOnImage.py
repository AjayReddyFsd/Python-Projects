from PIL import Image, ImageDraw, ImageFont


def writeTextOnImage():
    imgPath = r"C:\Users\ajaya\OneDrive\Desktop\GitHub Repos\Python-Projects\Image Processing\Image Files\celebration.jpg"
    img = Image.open(imgPath)

    coordinates = (0, 0)
    textToBeWritten = 'Happy Coding!'
    # one of the windows-11 fonts, must write in lower-case
    fontStyle = ImageFont.truetype('sylfaen.ttf', 50)
    color = (255, 255, 0)
    ImageDraw.Draw(img).text(
        coordinates, textToBeWritten, font=fontStyle, fill=color)

    img.show()


writeTextOnImage()
