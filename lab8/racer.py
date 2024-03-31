import pygame, sys, random, time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

Black = pygame.Color(0,0,0)
White = pygame.Color(255,255,255)
Grey = pygame.Color(128,128,128)
Red = pygame.Color(255,0,0)
Blue = pygame.Color(0, 0, 255)
Green = pygame.Color(0, 255, 0)


Screen_wid = 400
Screen_len = 600
Speed = 5
Score = 0
Coin_score = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("game over", True, Black)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((300,300))
DISPLAYSURF.fill(White)
pygame.display.set_caption("game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.inage.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Screen_wid-40),0)

    def move(self):
        global Score
        self.rect.move_ip(0,Speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, Screen_wid-40),0)

class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.left < Screen_wid:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
    
    def coins(self, coins):
        collisions = pygame.sprite.spritecollide(self, coins, True)
        for coin in collisions:
            return True
        return False
    
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Screen_wid - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, Speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, Screen_wid - 40), 0)


Player1 = Player()
Enemy1 = Enemy()
Coin1 = Coin()

Enemies = pygame.sprite.Group()
Enemies.add(Enemy1)
Coins = pygame.sprite.Group()
Coins.add(Coin1)
all_sprites = pygame.sprite.Group()
all_sprites.add(Player1)
all_sprites.add(Enemy1)
all_sprites.add(Coin1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            Speed += 0.5

        if event.type == quit:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(White)
    scores = font_small.render(str(Score), True, Black)
    coin_scores = font_small.render(str(Coin_score), True, Black)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_scores, (375, 10))
    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    if Player1.collect_coin(Coins):
        Coin_score += 1
        new_coin = Coin()
        Coins.add(new_coin)
        all_sprites.add(new_coin)

    if pygame.sprite.spritecollideany(Player1, Enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.asleep(0.5)

        DISPLAYSURF.fill(Red)
        DISPLAYSURF.blit(game_over, (30,250))

        pygame.diaplay.update()
        for entity in all.sprites:
            entity.kill()
        time.asleep(2)
        pygame.quit()
        sys.exit()


    pygame.diaplay.update()
    FramePerSec.tick(FPS)