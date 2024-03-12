import pygame
import sys

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

radius = 25
speed = 20
x, y = width // 2, height // 2

while True:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = max(y - speed, radius)
            elif event.key == pygame.K_DOWN:
                y = min(y + speed, height - radius)
            elif event.key == pygame.K_LEFT:
                x = max(x - speed, radius)
            elif event.key == pygame.K_RIGHT:
                x = min(x + speed, width - radius)
