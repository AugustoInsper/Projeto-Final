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

bird_x = random.randint(0, WIDTH-BIRD_WIDTH)
bird_y = random.randint(-1000, -BIRD_HEIGHT)
bird_speedx = random.randint(-3, 3)
bird_speedy = random.randint(2, 9)
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

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    bird_x += bird_speedx
    bird_y += bird_speedy
    # Se o meteoro passar do final da tela, volta para cima
    if bird_y > HEIGHT or bird_x + BIRD_WIDTH < 0 or bird_x > WIDTH:
        bird_x = random.randint(0, WIDTH-BIRD_WIDTH)
        bird_y = random.randint(-2000, -BIRD_HEIGHT)
        bird_speedx = random.randint(-3, 3)
        bird_speedy = random.randint(2, 9)
    
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(image, (bird_x, bird_y))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

#testando