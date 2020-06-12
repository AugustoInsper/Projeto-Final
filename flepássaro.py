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
pygame.display.set_caption('Flepássaro')
 
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
for i in range(49):
    # Os arquivos de animação são numerados de 00 a 48
    filename = 'forest frames/frame{}.jpg'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (int(WIDTH), int(HEIGHT)))
    background_anim.append(img)
assets["background_anim"] = background_anim

player_anim = []
for i in range(73):
    # Os arquivos de animação são numerados de 00 a 72
    filename = 'red_bird_frames/oie_transparent ({}).png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (BIRD_WIDTH, BIRD_HEIGHT))   # pegar dimensões do passarinho
    player_anim.append(img)
assets["player_anim"] = player_anim
assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)


class Player(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.player_anim = assets['player_anim']
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.player_anim[self.frame]  # Pega a primeira imagem
        self.mask = pygame.mask.from_surface(self.image)
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
        if self.rect.top < 0:
            self.rect.top = 0

            
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
        self.rect.x = 1100
        self.rect.y = 0
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx


class Treedown(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['tronco']
        self.rect = self.image.get_rect()
        self.rect.x = 1100
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
all_trees = pygame.sprite.Group()

player = Player((bird_x, bird_y), assets)
background = Background((0, 0), assets)
treeup1 = Treeup(assets)
treedown1 = Treedown(assets)

all_trees.add(treeup1)
all_trees.add(treedown1)

all_sprites.add(background)
all_sprites.add(player)
all_sprites.add(treeup1)
all_sprites.add(treedown1)

treeup1.rect.y = random.randint(-TREE_HEIGHT, 0)
treedown1.rect.y = treeup1.rect.y + TREE_HEIGHT + 164

tup2 = False
score = 0

# ===== Loop principal =====
while game:

    if treeup1.rect.x == 500:
        treeup2 = Treeup(assets)
        treedown2 = Treedown(assets)

        all_sprites.add(treeup2)
        all_sprites.add(treedown2)
        all_trees.add(treeup2)
        all_trees.add(treedown2)


        treeup2.rect.y = random.randint(-TREE_HEIGHT, 0)
        treedown2.rect.y = treeup2.rect.y + TREE_HEIGHT + 164

        treeup2.speedx = -1.5
        treedown2.speedx = -1.5

        tup2 = True


    if tup2:
        if treeup2.rect.x == 500:
            treeup1 = Treeup(assets)
            treedown1 = Treedown(assets)

            all_sprites.add(treeup1)
            all_sprites.add(treedown1)
            all_trees.add(treeup1)
            all_trees.add(treedown1)

            treeup1.rect.y = random.randint(-TREE_HEIGHT, 0)
            treedown1.rect.y = treeup1.rect.y + TREE_HEIGHT + 164

            treeup1.speedx = -1.5
            treedown1.speedx = -1.5 


    if treeup1.rect.x == bird_x or treeup2.rect.x == bird_x:
        score += 10


    hits = pygame.sprite.spritecollide(player, all_trees, True)
    if len(hits) > 0:
        game = False   

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências:
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.speedy = -1.3
                treeup1.speedx = -1.5
                treedown1.speedx = -1.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.speedy = 1.7

    all_sprites.update()
 
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    all_sprites.draw(window)


    text_surface = assets['score_font'].render("{:06d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)
 
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
