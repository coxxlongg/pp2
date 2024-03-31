import pygame

pygame.init()

width, height = 800, 600
menu_height = 70
white = (255, 255, 255)
black = (0, 0, 0)
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("paint")
clock = pygame.time.Clock()

active_figure = 0
active_color = white
painting = []

def draw_menu(active_color):
    screen.fill('gray', (0, 0, width, menu_height))
    pygame.draw.line(screen, black, (0, menu_height), (width, menu_height), 3)

    colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
              (0, 255, 255), (255, 0, 255), (0, 0, 0), white]
    color_rects = [pygame.Rect(width - 35 - i * 25, 10 if i % 2 == 0 else 35, 25, 25) for i in range(len(colors))]
    for color, rect in zip(colors, color_rects):
        pygame.draw.rect(screen, color, rect)

    brush_rects = [pygame.Rect(10 + i * 60, 10, 50, 50) for i in range(2)]
    for rect in brush_rects:
        pygame.draw.rect(screen, black, rect)
    pygame.draw.circle(screen, white, (35, 35), 20)
    pygame.draw.rect(screen, white, (70, 26, 37, 20), 2)

    return color_rects, brush_rects

def draw_painting(paints):
    for color, pos, figure in paints:
        if color == white:
            pygame.draw.rect(screen, white, (pos[0] - 15, pos[1] - 15, 37, 20))
        else:
            if figure == 0:
                pygame.draw.circle(screen, color, pos, 20, 2)
            elif figure == 1:
                pygame.draw.rect(screen, color, (pos[0] - 15, pos[1] - 15, 37, 20), 2)

running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if mouse_pos[1] > menu_height:
                painting.append((active_color, mouse_pos, active_figure))
            else:
                for i, color_rect in enumerate(color_rects):
                    if color_rect.collidepoint(mouse_pos):
                        active_color = colors[i]
                for i, brush_rect in enumerate(brush_rects):
                    if brush_rect.collidepoint(mouse_pos):
                        active_figure = i

    screen.fill(white)

    color_rects, brush_rects = draw_menu(active_color)

    draw_painting(painting)

    pygame.display.flip()

pygame.quit()

