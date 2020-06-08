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
TREE_WIDTH = 108
TREE_HEIGHT = 90
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('source.gif').convert()
background = pygame.transform.scale(background, (1000, 600))
bird = pygame.image.load('red_bird.gif').convert_alpha()
bird = pygame.transform.scale(bird, (BIRD_WIDTH, BIRD_HEIGHT))
tree = pygame.image.load('arvore.jpg').convert_alpha()
tree = pygame.transform.scale(tree, (TREE_WIDTH, TREE_HEIGHT))
 
# ----- Inicia estruturas de dados
game = True
 
bird_x = 250
bird_y = 300
bird_speedy = 0
 
tree_x = 850
tree_y = - HEIGHT + TREE_HEIGHT
 
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_speedy = 10
 
    bird_y += bird_speedy
 
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(bird, (bird_x, bird_y))
    window.blit(tree, (tree_x, tree_y))
 
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

#teste python
