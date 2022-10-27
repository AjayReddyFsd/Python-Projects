from PIL import Image


def createChessBoardImage():
    chessBoard = Image.new('RGB', (640, 640), (245, 218, 174))
    brownBlock = Image.new('RGB', (80, 80), (186, 97, 43))

    for i in range(4):
        chessBoard.paste(brownBlock, (160*i, 0))
        chessBoard.paste(brownBlock, (80+160*i, 80))

    for i in range(3):
        chessBoard.paste(chessBoard, (0, 160*i))

    chessBoard.show()


createChessBoardImage()
