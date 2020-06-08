# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# ----- Inicia assets
BIRD_WIDTH = 125
BIRD_HEIGHT = 103
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('source.gif').convert()
background = pygame.transform.scale(background, (1000, 600))
image = pygame.image.load('red_bird.gif').convert_alpha()
image = pygame.transform.scale(image, (BIRD_WIDTH, BIRD_HEIGHT))

# ----- Inicia estruturas de dados
game = True
# gravity = False

bird_x = 250
bird_y = 300
#bird_speedx = 0
bird_speedy = 0

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speedy = -10
#                gravity = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_speedy = 10

    # ----- Atualiza estado do jogo
    # Atualizando a posição do player
    
    # Se o player passar do final da tela, volta para cima
#    if gravity:
        # bird_x = 250
        # bird_y = -BIRD_HEIGHT
        # bird_speedx = 0
#        bird_speedy = 8

    # bird_x += bird_speedx
    bird_y += bird_speedy    

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(image, (bird_x, bird_y))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados