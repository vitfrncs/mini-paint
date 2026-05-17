from PIL import Image, ImageDraw
import numpy as np
from cores import *

class Button:
    def __init__(self, x1, y1, x2, y2, cor, funcao, descricao=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor_fundo = cor
        self.funcao = funcao
        self.descricao = descricao

    def foi_clicado(self, x, y):
        return self.x1 < x < self.x2 and self.y1 < y < self.y2

    def desenhar_botao(self, canvas):
        canvas.pixels[self.y1:self.y2, self.x1:self.x2] = self.cor_fundo

        if self.descricao is not None:
            # cria imagem do tamanho do botão para escrever o texto
            largura = self.x2 - self.x1
            altura = self.y2 - self.y1
            img = Image.new("RGB", (largura, altura), self.cor_fundo)

            draw = ImageDraw.Draw(img)
            draw.text((5, altura // 4), self.descricao, fill=(0, 0, 0))

            # copiar pixels da imagem para o canva
            pixels = np.array(img)
            for dy in range(altura):
                for dx in range(largura):
                    canvas.put_pixel(self.x1 + dx, self.y1 + dy, pixels[dy][dx])
        # desenhar a borda
        canvas.pixels[self.y1, self.x1:self.x2+1] = PRETO
        canvas.pixels[self.y2, self.x1:self.x2+1] = PRETO
        canvas.pixels[self.y1:self.y2, self.x1] = PRETO
        canvas.pixels[self.y1:self.y2, self.x2] = PRETO