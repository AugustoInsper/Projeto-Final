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
TREE_HEIGHT = 300                                                            

font = pygame.font.SysFont(None, 48)                                         
background = pygame.image.load('source.gif').convert()                       
background = pygame.transform.scale(background, (1000, 600))
bird = pygame.image.load('red_bird.png').convert_alpha()
bird = pygame.transform.scale(bird, (BIRD_WIDTH, BIRD_HEIGHT))
treedown = pygame.image.load('tronco.png').convert_alpha()
treedown = pygame.transform.scale(treedown, (TREE_WIDTH, TREE_HEIGHT))
treeup = pygame.image.load('tronco.png').convert_alpha()
treeup = pygame.transform.scale(treeup, (TREE_WIDTH, TREE_HEIGHT))

# ----- Inicia estruturas de dados
game = True
 
bird_x = 250
bird_y = 200
bird_speedy = 0
 
trees_x = 850
treeup_y = random.randint(-10, 0)
treedown_y = treeup_y + TREE_HEIGHT + 60
trees_speedx = 0

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
                trees_speedx = -8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_speedy = 5
                trees_speedx = -8

    if bird_y == 350 or bird_y < -100:
        game = False

#   space = random.randint

    bird_y += bird_speedy
    trees_x += trees_speedx
 
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(bird, (bird_x, bird_y))
    window.blit(treedown, (trees_x, treedown_y))
    window.blit(treeup, (trees_x, treeup_y))
 
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizadoss

