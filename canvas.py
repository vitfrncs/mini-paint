import numpy as np
from config import *
from PIL import Image
import time

# As coordenadas no canvas ficam trocadas pois o y cresce para baixo

class Canvas:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.espessura = 4
        self.cor_atual = PRETO
        self.ferramenta_atual = "lapis"
        self.pixels = np.ones((altura, largura, 3), dtype=np.uint8) * 255
        self.backup = None

    def put_pixel(self, x, y, cor):
        """Pixel na posição (x,y) recebe cor do argumento"""
        if 0 <= x < self.largura and 0 <= y < self.altura:
            self.pixels[y][x] = cor

    def get_pixel(self, x, y):
        """Retorna cor do pixel na posição (x,y)."""
        if 0 <= x < self.largura and ALTURA_BARRA_NAVEGACAO <= y < self.altura:
            return tuple(self.pixels[y][x])
        return None

    def limpar(self):
        """Apaga o que está na tela."""
        self.pixels[ALTURA_BARRA_NAVEGACAO:, :] = 255

    def salvar(self):
        """Salva imagem da tela em .png."""
        img = Image.fromarray(self.pixels[ALTURA_BARRA_NAVEGACAO:ALTURA, :, :])
        ts = int(time.time())
        img.save(f"images/{ts}.png")

    def salvar_estado(self):
        """Salva estado atual em backup. É usado na implementação do preview."""
        self.backup = self.pixels.copy()  # copia o array inteiro

    def restaurar_estado(self):
        """Restaura desenho da tela de acordo com as informações do backup."""
        if self.backup is not None:
            self.pixels[:] = self.backup  # volta para a cópia

    def pintar(self, x, y):
        """Pinta o pixel na posição (x,y) com a cor atual do canvas
           Caso a borracha esteja selecionada, ignora a cor atual e utiliza a cor branca."""
        if self.ferramenta_atual == "borracha":
            cor = BRANCO
        else:
            cor = self.cor_atual
        for dy in range(-self.espessura, self.espessura):
            for dx in range(-self.espessura, self.espessura):
                self.put_pixel(int(x) + dx, int(y) + dy, cor)

    def bresenham_linha(self, x1, y1, x2, y2):
        """Desenha uma linha entre os pontos (x1,y1) e (x2,y2) utilizando o algoritmo de Bresenham."""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        passos_x = 1 if x1 < x2 else -1
        passos_y = 1 if y1 < y2 else -1

        x, y = x1, y1

        # Se linha seja mais horizontal que vertical:
        if dx > dy:

            pant = 2 * dy - dx  # parâmetro de decisão de Bresenham

            # Percorre todos os pixels da direção x
            for _ in range(dx):
                self.pintar(x, y)

                # se o próximo pixel continua na mesma linha
                if pant < 0:
                    pant += 2 * dy

                # caso contrário, avança também no eixo y
                else:
                    pant += 2 * dy - 2 * dx
                    y += passos_y

                x += passos_x  # avança no eixo x

        # Se a linha seja mais vertical que horizontal
        else:
            pant = 2 * dx - dy

            # Percorre todos os pixels da direção y
            for _ in range(dy):
                self.pintar(x, y)

                # mantém a posição em x
                if pant < 0:
                    pant += 2 * dx

                # avança também no eixo x
                else:
                    pant += 2 * dx - 2 * dy
                    x += passos_x

                y += passos_y


    def desenhar_retangulo(self, x1, y1, x2, y2):
        self.bresenham_linha(x1, y1, x2, y1)
        self.bresenham_linha(x1, y2, x2, y2)
        self.bresenham_linha(x1, y1, x1, y2)
        self.bresenham_linha(x2, y1, x2, y2)


    def desenhar_retangulo_preenchido(self, x1, y1, x2, y2):
        xa, xb = min(x1, x2), max(x1, x2)
        ya, yb = min(y1, y2), max(y1, y2)
        self.pixels[ya:yb, xa:xb] = self.cor_atual

    def bresenham_circulo(self, x1, y1, x2, y2):

        raio = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5) # calcula raio usando a distância entre o centro e o ponto 2

        # topo do círculo
        x = 0
        y = raio
        d = 1 - raio # parametro de decisão

        # Desenha o primeiro conjunto de pontos
        if self.ferramenta_atual == "circulo":
            self.plotaOctetos(x1, y1, x, y)

        elif self.ferramenta_atual == "circulo_preenchido":
            self._preencher_linha(x1, y1, x, y)

        while x <= y:

            # Escolhe o próximo pixel do círculo
            if d < 0:
                d += 2 * x + 3

            else:
                d += 2 * (x - y) + 5
                y -= 1

            x += 1

            # Desenha apenas a borda
            if self.ferramenta_atual == "circulo":
                self.plotaOctetos(x1, y1, x, y)

            # Desenha preenchido
            elif self.ferramenta_atual == "circulo_preenchido":
                self._preencher_linha(x1, y1, x, y)


    def plotaOctetos(self, x1, y1, x, y):
        self.pintar(x1 + x, y1 + y)
        self.pintar(x1 - x, y1 + y)
        self.pintar(x1 + x, y1 - y)
        self.pintar(x1 - x, y1 - y)
        self.pintar(x1 + y, y1 + x)
        self.pintar(x1 - y, y1 + x)
        self.pintar(x1 + y, y1 - x)
        self.pintar(x1 - y, y1 - x)


    def _preencher_linha(self, cx, cy, x, y):
        self.linha(cy + y, cx - x, cx + x)
        self.linha(cy - y, cx - x, cx + x)
        self.linha(cy + x, cx - y, cx + y)
        self.linha(cy - x, cx - y, cx + y)

    def linha(self, py, xa, xb):
        if 0 <= py < self.altura:
            xa = max(0, xa)
            xb = min(self.largura, xb)
            if xa < xb:
                self.pixels[py, xa:xb] = self.cor_atual

    def balde_tinta(self, x, y):
        cor_pixel = self.get_pixel(x, y)

        if cor_pixel is None:
            return

        if cor_pixel == self.cor_atual:
            return

        fila = [(x, y)] # Pontos a serem  processados
        visitados = set() # Armazena pixels já processados

        while fila:
            # Remove um pixel da pilha
            cx, cy = fila.pop()

            # Ignora pixels já visitados
            if (cx, cy) in visitados:
                continue

            # Ignora pixels de outra cor
            if self.get_pixel(cx, cy) != cor_pixel:
                continue

            self.put_pixel(cx, cy, self.cor_atual)

            # Marca como visitado
            visitados.add((cx, cy))

            # Adiciona os 4 vizinhos na fila para serem visitados
            if not ((cx + 1, cy) in visitados): fila.append((cx + 1, cy))
            if not ((cx - 1, cy) in visitados): fila.append((cx - 1, cy))
            if not ((cx, cy + 1) in visitados): fila.append((cx, cy + 1))
            if not ((cx, cy - 1) in visitados): fila.append((cx, cy - 1))