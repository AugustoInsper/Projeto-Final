# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time
 
pygame.init()
 
# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')
 
# ----- Inicia assets
BIRD_WIDTH = 100
BIRD_HEIGHT = 82
TREE_WIDTH = 108
TREE_HEIGHT = HEIGHT - 123

assets = {}
# font = pygame.font.SysFont(None, 48)

assets['tronco'] = pygame.image.load('tronco.png').convert_alpha()
assets['tronco'] = pygame.transform.scale(assets['tronco'], (TREE_WIDTH, TREE_HEIGHT))

background_anim = []
win_rect = window.get_rect()
for i in range(60):
    # Os arquivos de animação são numerados de 00 a 59
    filename = 'source frames/frame_{}_delay-0.1s.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (int(2*WIDTH), int(2*HEIGHT)))
    background_anim.append(img)
assets["background_anim"] = background_anim

player_anim = []
for i in range(73):
    # Os arquivos de animação são numerados de 00 a 72
    filename = 'red bird frames/{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (BIRD_WIDTH, BIRD_HEIGHT))   # pegar dimensões do passarinho
    player_anim.append(img)
assets["player_anim"] = player_anim


class Player(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.player_anim = assets['player_anim']
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.player_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50
        self.speedy = 0

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
            # Avança um quadro.
            self.frame += 1

            if self.frame == len(self.player_anim):
                self.frame = 0
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.player_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

            
class Background(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.background_anim = assets['background_anim']
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.background_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50

    
    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
            # Avança um quadro.
            self.frame += 1

            if self.frame == len(self.background_anim):
                self.frame = 0
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.background_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Treeup(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['tronco']
        self.rect = self.image.get_rect()
        self.rect.x = 850
        self.rect.y = 0
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx


class Treedown(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['tronco']
        self.rect = self.image.get_rect()
        self.rect.x = 850
        self.rect.y = 0
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx


# ----- Inicia estruturas de dados
game = True
 
bird_x = 250
bird_y = 200
bird_speedy = 0

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
player = Player((bird_x, bird_y), assets)
background = Background((0, 0), assets)
treeup = Treeup(assets)
treedown = Treedown(assets)
all_sprites.add(background)
all_sprites.add(player)
all_sprites.add(treeup)
all_sprites.add(treedown)

treeup.rect.y = random.randint(-TREE_HEIGHT, 0)
treedown.rect.y = treeup.rect.y + TREE_HEIGHT + 123
# ===== Loop principal =====
while game:
    
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.speedy = -10
                treeup.speedx = -8
                treedown.speedx = -8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.speedy = 10
                treeup.speedx = -8
                treedown.speedx = -8

    all_sprites.update()
 
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    all_sprites.draw(window)
 
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados