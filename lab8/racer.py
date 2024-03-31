import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

# Constants
FPS = 60
Screen_wid = 400
Screen_len = 600
Score = 0
Coin_score = 0

# Colors
Black = pygame.Color(0, 0, 0)
White = pygame.Color(255, 255, 255)
Red = pygame.Color(255, 0, 0)

# Fonts
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font_small.render("Game Over", True, Black)

# Load images
enemy_image_path = "/Users/coxlong/Downloads/Enemy.png"
player_image_path = "/Users/coxlong/Downloads/Player.png"
coin_image_path = "/Users/coxlong/Downloads/Screenshot 2024-03-31 at 21.36.36 2 Background Removed.png"

# Set up display
DISPLAYSURF = pygame.display.set_mode((Screen_wid, Screen_len))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(enemy_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Screen_wid - 40), 0)

    def move(self):
        self.rect.move_ip(0, Speed)
        if self.rect.bottom > Screen_len:
            self.rect.top = 0
            self.rect.center = (random.randint(40, Screen_wid - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(player_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < Screen_wid:  # Fixed condition to check right side
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    def collect_coin(self, coins):
        collisions = pygame.sprite.spritecollide(self, coins, True)
        for coin in collisions:
            return True
        return False
    
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(coin_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Screen_wid - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, Speed)
        if self.rect.top > Screen_len:
            self.rect.top = 0
            self.rect.center = (random.randint(40, Screen_wid - 40), 0)

# Initialize game objects
Player1 = Player()
Enemy1 = Enemy()
Coin1 = Coin()

# Sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(Player1)
all_sprites.add(Enemy1)
all_sprites.add(Coin1)

# Custom event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            Speed += 0.5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player and enemies
    for entity in all_sprites:
        entity.move()

    # Check for collisions
    if Player1.collect_coin([Coin1]):
        Coin_score += 1
        new_coin = Coin()
        all_sprites.add(new_coin)

    if pygame.sprite.spritecollideany(Player1, [Enemy1]):
        time.sleep(0.5)
        DISPLAYSURF.fill(Red)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Draw everything
    DISPLAYSURF.fill(White)
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Display scores
    scores = font_small.render(f"Score: {Score}", True, Black)
    coin_scores = font_small.render(f"Coins: {Coin_score}", True, Black)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (375, 10))

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
