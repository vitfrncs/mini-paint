from button import *
from config import *
from cores import *

class UI:
    def __init__(self, canvas):
        self.canvas = canvas
        self.botoes = []
        self._criar_botoes()

    def _criar_botoes(self):
        definicoes = [
            # Novo e Salvar
            (X_NS, LINHA1_Y1, X_NS+BTT_LARGURA, LINHA1_Y2, CINZA, "limpar", "N"),
            (X_NS, LINHA2_Y1, X_NS+BTT_LARGURA, LINHA2_Y2, CINZA, "salvar", "S"),

            # Ferramentas
            (X_TOOLS+(BTT_LARGURA+MARGEM)*0, LINHA1_Y1, X_TOOLS+(BTT_LARGURA+MARGEM)*0+BTT_LARGURA, LINHA1_Y2, CINZA, "lapis",    "L"),
            (X_TOOLS+(BTT_LARGURA+MARGEM)*0, LINHA2_Y1, X_TOOLS+(BTT_LARGURA+MARGEM)*0+BTT_LARGURA, LINHA2_Y2, CINZA, "borracha", "B"),
            (X_TOOLS+(BTT_LARGURA+MARGEM)*1, LINHA1_Y1, X_TOOLS+(BTT_LARGURA+MARGEM)*1+BTT_LARGURA, LINHA1_Y2, CINZA, "linha",    "Li"),
            (X_TOOLS+(BTT_LARGURA+MARGEM)*1, LINHA2_Y1, X_TOOLS+(BTT_LARGURA+MARGEM)*1+BTT_LARGURA, LINHA2_Y2, CINZA, "balde",    "BT"),
            (X_TOOLS+(BTT_LARGURA+MARGEM)*2, LINHA1_Y1, X_TOOLS+(BTT_LARGURA+MARGEM)*2+BTT_LARGURA, LINHA1_Y2, CINZA, "retangulo",           "RV"),
            (X_TOOLS+(BTT_LARGURA+MARGEM)*2, LINHA2_Y1, X_TOOLS+(BTT_LARGURA+MARGEM)*2+BTT_LARGURA, LINHA2_Y2, CINZA, "retangulo_preenchido", "RP"),
            (X_TOOLS+(BTT_LARGURA+MARGEM)*3, LINHA1_Y1, X_TOOLS+(BTT_LARGURA+MARGEM)*3+BTT_LARGURA, LINHA1_Y2, CINZA, "circulo",             "CV"),
            (X_TOOLS+(BTT_LARGURA+MARGEM)*3, LINHA2_Y1, X_TOOLS+(BTT_LARGURA+MARGEM)*3+BTT_LARGURA, LINHA2_Y2, CINZA, "circulo_preenchido",  "CP"),

            # Espessuras
            (X_ESP, LINHA1_Y1,          X_ESP+BTT_LARGURA, LINHA1_Y1+TERCO-MARGEM,  PRETO, "fino",   None),
            (X_ESP, LINHA1_Y1+TERCO,    X_ESP+BTT_LARGURA, LINHA1_Y1+TERCO*2-MARGEM,PRETO, "medio",  None),
            (X_ESP, LINHA1_Y1+TERCO*2,  X_ESP+BTT_LARGURA, LINHA2_Y2,               PRETO, "grosso", None),
        ]

        for x1, y1, x2, y2, cor, funcao, descricao in definicoes:
            self.botoes.append(Button(x1, y1, x2, y2, cor, funcao, descricao))

        # Cores
        for i, cor in enumerate(PALETA):
            coluna = i % 5
            linha  = i // 5
            x0 = X_CORES + coluna * (COR_W + MARGEM)
            y0 = LINHA1_Y1 if linha == 0 else LINHA2_Y1
            self.botoes.append(Button(x0, y0, x0+COR_W, y0+BTT_ALTURA, cor, cor, None))

    def botao_clicado(self, x, y):
        """Retorna a função do botão clicado."""
        for botao in self.botoes:
            if botao.foi_clicado(x, y):
                return botao.funcao
        return None

    def desenhar_barra_navegacao(self):
        self.canvas.pixels[:ALTURA_BARRA_NAVEGACAO, :] = CINZA
        for botao in self.botoes:
            botao.desenhar_botao(self.canvas)