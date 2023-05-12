from PIL import Image


class VerImagem:

    def __init__(self):
        pass

    def visualizar_imagem(self):
        imagem = Image.open('man.jpg')
        imagem.show()

