import glfw
from OpenGL.GL import *
from canvas import *
from config import *
from ui import UI

canvas = Canvas(LARGURA, ALTURA)
ferramentas_2_cliques = ["linha", "retangulo", "retangulo_preenchido", "circulo", "circulo_preenchido"]
mouse_pressionado = False
aguardando_segundo_clique = False
x_inicio, y_inicio = 0, 0
ui = UI(canvas)

def mouse_botao_callback(window, botao, acao, mods):
    """Processa o clique do mouse e chama a ação correspondente ao botão pressionado por último."""
    global mouse_pressionado, x_inicio, y_inicio, aguardando_segundo_clique
    if botao == glfw.MOUSE_BUTTON_LEFT and acao == glfw.PRESS:
        x = int(glfw.get_cursor_pos(window)[0])
        y = int(glfw.get_cursor_pos(window)[1])

        if y < ALTURA_BARRA_NAVEGACAO:
            aguardando_segundo_clique = False
            processar_acao(ui.botao_clicado(x, y))
            return

        if canvas.ferramenta_atual in ferramentas_2_cliques:
            if not aguardando_segundo_clique:
                x_inicio, y_inicio = x, y
                canvas.salvar_estado()
                aguardando_segundo_clique = True
            else:
                aguardando_segundo_clique = False
                processar_acao(canvas.ferramenta_atual, x_inicio, y_inicio, x, y)
        else:
            mouse_pressionado = True
            if canvas.ferramenta_atual == "lapis":
                canvas.pintar(x, y)
            elif canvas.ferramenta_atual == "balde":
                canvas.balde_tinta(x, y)

    elif acao == glfw.RELEASE:
        mouse_pressionado = False

def mouse_posicao_callback(window, x, y):
    """Processa a posição do mouse."""
    x, y = int(x), int(y)

    if aguardando_segundo_clique:
        canvas.restaurar_estado()
        processar_acao(canvas.ferramenta_atual, x_inicio, y_inicio, x, y)
        return

    if mouse_pressionado and y >= ALTURA_BARRA_NAVEGACAO:
        canvas.pintar(x, y)

FERRAMENTAS_2_CLIQUES = ["linha", "retangulo", "retangulo_preenchido", "circulo", "circulo_preenchido"]

def processar_acao(acao, x1=None, y1=None, x2=None, y2=None):
    """Chama a função correspondente ao último botão selecionado"""
    if acao is None:
        return
    elif acao == "limpar":
        canvas.limpar()
    elif acao == "salvar":
        canvas.salvar()
    elif acao == "fino":
        canvas.espessura = ESPESSURA_FINA
    elif acao == "medio":
        canvas.espessura = ESPESSURA_MEDIA
    elif acao == "grosso":
        canvas.espessura = ESPESSURA_GROSSA
    elif acao in FERRAMENTAS_2_CLIQUES and x1 is not None:  # só desenha se tiver coordenadas
        if acao == "linha":
            canvas.bresenham_linha(x1, y1, x2, y2)
        elif acao == "retangulo":
            canvas.desenhar_retangulo(x1, y1, x2, y2)
        elif acao == "retangulo_preenchido":
            canvas.desenhar_retangulo_preenchido(x1, y1, x2, y2)
        elif acao == "circulo" or acao == "circulo_preenchido":
             canvas.bresenham_circulo(x1, y1, x2, y2)
    elif isinstance(acao, tuple):
        canvas.cor_atual = acao
    else:
        canvas.ferramenta_atual = acao

def init():
    glClearColor(1, 1, 1, 1)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    ui.desenhar_barra_navegacao()
    glDrawPixels(LARGURA, ALTURA, GL_RGB, GL_UNSIGNED_BYTE, np.flipud(canvas.pixels))

def main():
    glfw.init()
    window = glfw.create_window(LARGURA, ALTURA, 'Mini Paint', None, None)
    glfw.make_context_current(window)

    # processando cliques de acordo com botão selecionado
    glfw.set_mouse_button_callback(window, mouse_botao_callback)
    glfw.set_cursor_pos_callback(window, mouse_posicao_callback)

    init()
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

if __name__ == "__main__":
    main()
    glfw.terminate()