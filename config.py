#Definição de configurações gerais da janela

from cores import *

LARGURA = 800
ALTURA = 600
# ALTURA_BARRA_NAVEGACAO = 100

ESPESSURA_FINA   = 2
ESPESSURA_MEDIA  = 3
ESPESSURA_GROSSA = 8

#Definição dos botoes do menu

BTT_LARGURA = 35
BTT_ALTURA = 35
MARGEM = 5
GAP = 25

# Linha 1 e linha 2 do menu
LINHA1_Y1 = 8
LINHA1_Y2 = LINHA1_Y1 + BTT_ALTURA
LINHA2_Y1 = LINHA1_Y2 + MARGEM
LINHA2_Y2 = LINHA2_Y1 + BTT_ALTURA
ALTURA_BARRA_NAVEGACAO = LINHA2_Y2 + 8

# X inicial de cada grupo
X_NS    = 8
X_TOOLS = X_NS    + BTT_LARGURA + GAP
X_ESP   = X_TOOLS + (BTT_LARGURA + MARGEM) * 4 + GAP
X_CORES = X_ESP   + BTT_LARGURA + GAP

# Altura total das 2 linhas (para dividir espessuras em 3)
ALTURA_TOTAL  = LINHA2_Y2 - LINHA1_Y1
TERCO = ALTURA_TOTAL // 3

BOTOES = [
    # Novo e Salvar
    {"descricao": "N", "funcao": "limpar", "cor_fundo": CINZA, "x1": X_NS, "y1": LINHA1_Y1, "x2": X_NS + BTT_LARGURA, "y2": LINHA1_Y2},
    {"descricao": "S", "funcao": "salvar", "cor_fundo": CINZA, "x1": X_NS, "y1": LINHA2_Y1, "x2": X_NS + BTT_LARGURA, "y2": LINHA2_Y2},

    # Ferramentas
    {"descricao": "L", "funcao": "lapis", "cor_fundo": CINZA, "x1": X_TOOLS + (BTT_LARGURA+MARGEM)*0, "y1": LINHA1_Y1, "x2": X_TOOLS + (BTT_LARGURA+MARGEM)*0+BTT_LARGURA, "y2": LINHA1_Y2},
    {"descricao": "B",  "funcao": "borracha", "cor_fundo": CINZA, "x1": X_TOOLS + (BTT_LARGURA+MARGEM)*0, "y1": LINHA2_Y1, "x2": X_TOOLS + (BTT_LARGURA+MARGEM)*0+BTT_LARGURA, "y2": LINHA2_Y2},
    {"descricao": "Li", "funcao": "linha", "cor_fundo": CINZA, "x1": X_TOOLS + (BTT_LARGURA+MARGEM)*1,"y1": LINHA1_Y1, "x2": X_TOOLS + (BTT_LARGURA+MARGEM)*1+BTT_LARGURA, "y2": LINHA1_Y2},
    {"descricao": "BT", "funcao": "balde","cor_fundo": CINZA, "x1": X_TOOLS + (BTT_LARGURA+MARGEM)*1, "y1": LINHA2_Y1, "x2": X_TOOLS + (BTT_LARGURA+MARGEM)*1+BTT_LARGURA, "y2": LINHA2_Y2},
    {"descricao": "RV", "funcao": "retangulo","cor_fundo": CINZA, "x1": X_TOOLS + (BTT_LARGURA+MARGEM)*2,"y1": LINHA1_Y1, "x2": X_TOOLS + (BTT_LARGURA+MARGEM)*2+BTT_LARGURA, "y2": LINHA1_Y2},
    {"descricao": "RP", "funcao": "retangulo_preenchido", "cor_fundo": CINZA, "x1": X_TOOLS + (BTT_LARGURA+MARGEM)*2,"y1": LINHA2_Y1, "x2": X_TOOLS + (BTT_LARGURA+MARGEM)*2+BTT_LARGURA, "y2": LINHA2_Y2},
    {"descricao": "CV", "funcao": "circulo","cor_fundo": CINZA,"x1": X_TOOLS + (BTT_LARGURA+MARGEM)*3,"y1": LINHA1_Y1, "x2": X_TOOLS + (BTT_LARGURA+MARGEM)*3+BTT_LARGURA, "y2": LINHA1_Y2},
    {"descricao": "CP", "funcao": "circulo_preenchido",   "cor_fundo": CINZA, "x1": X_TOOLS + (BTT_LARGURA+MARGEM)*3,"y1": LINHA2_Y1,"x2": X_TOOLS + (BTT_LARGURA+MARGEM)*3+BTT_LARGURA, "y2": LINHA2_Y2},

    # Espessuras (3 linhas, x é maior)
    {"descricao": None, "funcao": "fino","cor_fundo": PRETO, "x1": X_ESP, "y1": LINHA1_Y1, "x2": X_ESP + BTT_LARGURA, "y2": LINHA1_Y1 + TERCO - MARGEM},
    {"descricao": None, "funcao": "medio",  "cor_fundo": PRETO, "x1": X_ESP, "y1": LINHA1_Y1 + TERCO, "x2": X_ESP + BTT_LARGURA, "y2": LINHA1_Y1 + TERCO*2 - MARGEM},
    {"descricao": None, "funcao": "grosso", "cor_fundo": PRETO,"x1": X_ESP, "y1": LINHA1_Y1 + TERCO*2, "x2": X_ESP + BTT_LARGURA, "y2": LINHA2_Y2},
]

COR_W = 25
BOTOES_CORES = []
for i, cor in enumerate(PALETA):
    coluna = i % 5
    linha  = i // 5
    x0 = X_CORES + coluna * (COR_W + MARGEM)
    y0 = LINHA1_Y1 if linha == 0 else LINHA2_Y1
    BOTOES_CORES.append({
        "descricao": None,
        "funcao":    cor,
        "cor_fundo": cor,
        "x1": x0,           "y1": y0,
        "x2": x0 + COR_W,   "y2": y0 + BTT_ALTURA,
    })

