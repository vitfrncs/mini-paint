from button import *
from config import *

class UI:
    def __init__(self, canvas):
        self.canvas = canvas
        self.botoes = []
        self._criar_botoes()

    def _criar_botoes(self):
        for b in BOTOES + BOTOES_CORES:
            self.botoes.append(
                Button(x1=b["x1"], y1=b["y1"], x2=b["x2"], y2=b["y2"],cor=b["cor_fundo"],
                    funcao=b["funcao"], descricao=b["descricao"]
                )
            )

    def botao_clicado(self, x, y):
        for botao in self.botoes:
            if botao.foi_clicado(x, y):
                return botao.funcao
        return None

    def desenhar_barra_navegacao(self):
        self.canvas.pixels[:ALTURA_BARRA_NAVEGACAO, :] = CINZA
        for botao in self.botoes:
            botao.desenhar_botao(self.canvas)