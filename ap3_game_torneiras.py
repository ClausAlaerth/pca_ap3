import pygame
import random
import time

pygame.init()

janela = pygame.display.set_mode([1050, 620])
pygame.display.set_caption("Feche as Torneiras!")

tela_de_titulo = pygame.image.load("assets_ap3/telas/titulo.png")

tela_nivel = pygame.image.load("assets_ap3/fundos/fundonv1.png")

parabens = pygame.image.load("assets_ap3/telas/parabens.jpg")

gameover = pygame.image.load("assets_ap3/telas/gameover.jpg")

score = 0

score_img = pygame.image.load("assets_ap3/botoes/pontuacao/0.png")

caixa_dagua = 30

caixa_img = pygame.image.load("assets_ap3/botoes/caixadagua/30.png")

torneira1 = pygame.image.load("assets_ap3/torneiras_fechadas/1.png")
torneira2 = pygame.image.load("assets_ap3/torneiras_fechadas/2.png")
torneira3 = pygame.image.load("assets_ap3/torneiras_fechadas/3.png")
torneira4 = pygame.image.load("assets_ap3/torneiras_fechadas/4.png")

torneira1_ab = pygame.image.load("assets_ap3/torneiras_abertas/1.png")
torneira2_ab = pygame.image.load("assets_ap3/torneiras_abertas/2.png")
torneira3_ab = pygame.image.load("assets_ap3/torneiras_abertas/3.png")
torneira4_ab = pygame.image.load("assets_ap3/torneiras_abertas/4.png")

lista_torneiras = ["torneira 1", "torneira 2", "torneira 3", "torneira 4"]

menu = True

aleatorio = True

timer = False

falha = False

concluir = False

fechado1 = True
fechado2 = True
fechado3 = True
fechado4 = True

loop = True


def ativacao():
    global fechado1, fechado2, fechado3, fechado4, caixa_dagua, caixa_img, aleatorio, timer

    starttime = time.time()

    if not menu:

        if aleatorio:

            if random.choice(lista_torneiras) == "torneira 1":
                fechado1 = False

            elif random.choice(lista_torneiras) == "torneira 2":
                fechado2 = False

            elif random.choice(lista_torneiras) == "torneira 3":
                fechado3 = False

            elif random.choice(lista_torneiras) == "torneira 4":
                fechado4 = False

            if not fechado1 or fechado2 or fechado3 or fechado4:

                time.sleep(1 - ((time.time() - starttime) % 1))
                caixa_dagua -= 1
                caixa_img = pygame.image.load(f"assets_ap3/botoes/caixadagua/{caixa_dagua}.png")
                print(caixa_dagua)

            if fechado1 and fechado2 and fechado3 and fechado4:
                if caixa_dagua <= 27:
                    print("pausa")
                    caixa_dagua += 3

            elif caixa_dagua == 0:

                aleatorio = False
                return


def eventos():
    global loop, menu, score_img, fechado1, fechado2, fechado3, fechado4, score

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RETURN:
                menu = False

        if not menu:

            if not falha:
                if not concluir:
                    if not fechado1:
                        if events.type == pygame.KEYDOWN:
                            if events.key == pygame.K_a:
                                fechado1 = True
                                score += 1
                                score_img = pygame.image.load(f"assets_ap3/botoes/pontuacao/{score}.png")

            if not falha:
                if not concluir:
                    if not fechado2:
                        if events.type == pygame.KEYDOWN:
                            if events.key == pygame.K_s:
                                fechado2 = True
                                score += 1
                                score_img = pygame.image.load(f"assets_ap3/botoes/pontuacao/{score}.png")

            if not falha:
                if not concluir:
                    if not fechado3:
                        if events.type == pygame.KEYDOWN:
                            if events.key == pygame.K_d:
                                fechado3 = True
                                score += 1
                                score_img = pygame.image.load(f"assets_ap3/botoes/pontuacao/{score}.png")

            if not falha:
                if not concluir:
                    if not fechado4:
                        if events.type == pygame.KEYDOWN:
                            if events.key == pygame.K_f:
                                fechado4 = True
                                score += 1
                                score_img = pygame.image.load(f"assets_ap3/botoes/pontuacao/{score}.png")


def game_over():
    global falha

    if not concluir:
        if caixa_dagua == 0:
            if score != 20:
                falha = True

                janela.blit(gameover, (0, 0))
                janela.blit(score_img, (500, 300))
                return


def desenho_na_tela():
    global score, menu, score_img, concluir, caixa_img

    if menu:
        janela.blit(tela_de_titulo, (0, 0))

    if not menu:
        janela.blit(tela_nivel, (0, 0))

        janela.blit(score_img, (500, 100))

        janela.blit(caixa_img, (20, 100))

        janela.blit(torneira1, (20, 440))
        janela.blit(torneira2, (250, 440))
        janela.blit(torneira3, (600, 440))
        janela.blit(torneira4, (830, 440))

        if not fechado1:
            janela.blit(torneira1_ab, (20, 440))

        if not fechado2:
            janela.blit(torneira2_ab, (250, 440))

        if not fechado3:
            janela.blit(torneira3_ab, (600, 440))

        if not fechado4:
            janela.blit(torneira4_ab, (830, 440))

        if score == 20:
            janela.blit(parabens, (0, 0))
            janela.blit(score_img, (500, 300))

            concluir = True
            return


while loop:

    desenho_na_tela()
    ativacao()
    eventos()
    game_over()
    pygame.display.update()
