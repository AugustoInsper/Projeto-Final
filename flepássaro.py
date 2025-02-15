# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flepássaro')

# ----- Dimensões dos sprites
BIRD_WIDTH = 100
BIRD_HEIGHT = 82
TREE_WIDTH = 108
TREE_HEIGHT = HEIGHT

# ----- Inicia assets
assets = {}
assets['tronco'] = pygame.image.load('imagens/tronco.png').convert_alpha()
assets['tronco'] = pygame.transform.scale(assets['tronco'], (TREE_WIDTH, TREE_HEIGHT))
background_anim = []

# No gif de onde foram pegos os seguintes frames, as árvores inicialmente estavam se movendo da esquerda para a direita,
# o que não faz sentido ao analisar a ideia de movimento em relação ao player que queremos passar, por isso
# tivemos que percorrer os frames de trás para frente
i=191
while i>=0:
    # Os arquivos de animação são numerados de 00 a 191
    filename = 'background_frames/frame{}-0000.jpg'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (int(WIDTH), int(HEIGHT)))
    background_anim.append(img)
    i-=1
assets["background_anim"] = background_anim

player_anim = []
for i in range(73):
    # Os arquivos de animação são numerados de 00 a 72
    filename = 'red_bird_frames/oie_transparent ({}).png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (BIRD_WIDTH, BIRD_HEIGHT))
    player_anim.append(img)
assets["player_anim"] = player_anim
assets["score_font"] = pygame.font.Font('fonte/PressStart2P.ttf', 28)


# Carrega os áudios do Flepássaro
pygame.mixer.music.load('Sons/background sound.wav')
pygame.mixer.music.set_volume(0.4)

# Inicia classes

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
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.center = center

        # Não permite que o player passe para cima e para baixo da janela
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
        self.rect.x = 0  # Posiciona o centro da imagem
        self.rect.y = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 100

    
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
                center = self.rect.center
                self.image = self.background_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Treeup(pygame.sprite.Sprite):             # Classe dos troncos que vão aparecer na parte de cima da tela
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['tronco']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 0
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx


class Treedown(pygame.sprite.Sprite):           # Classe dos troncos que vão aparecer na parte de baixo da tela
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['tronco']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 0
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx


# Inicia funções

def menu(screen):
    # Carrega o fundo da tela inicial
    inicio = pygame.image.load('Capa_flepassaro.jpg').convert()
    inicio = pygame.transform.scale(inicio, (1000, 389))
    inicio_rect = inicio.get_rect()

    inits = True
    while inits:
        # Processa os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inits = False
                state = CLOSE
            if event.type == pygame.KEYUP:
                inits = False
                state = GAME

        # A cada loop, redesenha o fundo e os sprites
        screen.fill((0, 0, 0))
        screen.blit(inicio, (0, HEIGHT/2 - int(389/2)))

        pygame.display.flip()
    return state


def gameover(screen): 
    # Carrega o fundo da tela inicial
    fim = pygame.image.load('imagens/perdeu.jpg').convert()
    fim = pygame.transform.scale(fim, (WIDTH, HEIGHT))
    fim_rect = fim.get_rect()

    finals = True

    while finals:
        for event in pygame.event.get():
            # Processa os eventos
            if event.type == pygame.QUIT:
                finals = False
                state = CLOSE
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    finals = False
                    state = CLOSE

        # A cada loop, redesenha o fundo e os sprites
        screen.fill((0, 0, 0))
        screen.blit(fim, fim_rect)

        # Escreve a pontuação na tela de Game Over
        text_surface = assets['score_font'].render("{:00d}".format(score), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        pygame.display.flip()
    return state


# ----- Inicia estruturas de dados
bird_x = 250
bird_y = 200

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

treeup1.rect.y = random.randint(-TREE_HEIGHT, -205)
treedown1.rect.y = treeup1.rect.y + TREE_HEIGHT + 205

tup2 = False
score = 0
trees_speedx = -1.0
player_speedy = 1.3

GAME = 0
CLOSE = 1
state = menu(window)
pygame.mixer.music.play(loops=-1)

# ===== Loop principal =====
while state == GAME:

    # Se a árvore 1 chega em determinado ponto x, é criada a ávore 2:
    if treeup1.rect.x == 650:
        treeup2 = Treeup(assets)
        treedown2 = Treedown(assets)

        all_sprites.add(treeup2)
        all_sprites.add(treedown2)
        all_trees.add(treeup2)
        all_trees.add(treedown2)


        treeup2.rect.y = random.randint(-TREE_HEIGHT, -205)
        treedown2.rect.y = treeup2.rect.y + TREE_HEIGHT + 205

        treeup2.speedx = trees_speedx
        treedown2.speedx = trees_speedx

        tup2 = True

    # Se a ávore 2 chega em determinado ponto x, a árvore 1 é recriada:
    if tup2:
        if treeup2.rect.x == 650:
            treeup1 = Treeup(assets)
            treedown1 = Treedown(assets)

            all_sprites.add(treeup1)
            all_sprites.add(treedown1)
            all_trees.add(treeup1)
            all_trees.add(treedown1)

            treeup1.rect.y = random.randint(-TREE_HEIGHT, -205)
            treedown1.rect.y = treeup1.rect.y + TREE_HEIGHT + 205

            treeup1.speedx = trees_speedx
            treedown1.speedx = trees_speedx

    if tup2:
        if treeup1.rect.x == bird_x or treeup2.rect.x == bird_x:
            score += 1

    # Casos em que o player perde o jogo:
    hits = pygame.sprite.spritecollide(player, all_trees, False, pygame.sprite.collide_mask)
    if len(hits) > 0:
        state = CLOSE

    if  player.rect.y == HEIGHT - BIRD_HEIGHT:
        state = CLOSE

    if  player.rect.y == 0:
        state = CLOSE

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências:
        if event.type == pygame.QUIT:
            state = CLOSE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.speedy = - player_speedy
                treeup1.speedx = trees_speedx
                treedown1.speedx = trees_speedx
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.speedy = player_speedy


    all_sprites.update()

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    all_sprites.draw(window)

    text_surface = assets['score_font'].render("{:00d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    # Se o estado é "CLOSE", começa a nova música para a tela de Game Over e chama a classe responsável por essa parte do jogo
    if state == CLOSE:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Sons/game over.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops = 0)

        gameover(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

