from PIL import Image


def createIndianFlagImage():
    flag = Image.new('RGB', (900, 600), (255, 255, 255))
    saffron = Image.new('RGB', (900, 200), (255, 153, 51))
    green = Image.new('RGB', (900, 200), (18, 136, 7))
    ashokaWheel = Image.open(r"C:\Users\ajaya\OneDrive\Desktop\GitHub Repos\Python-Projects\Image Processing\Image Files\ashokaWheel.png")

    flag.paste(saffron, (0, 0))
    flag.paste(green, (0, 400))
    flag.paste(ashokaWheel, (350, 200))

    flag.show()


createIndianFlagImage()
