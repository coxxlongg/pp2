import pygame
import random

pygame.init()

# Define constants
width, height = 600, 400
grid_size = 20
fps = 10

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define directions
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.position = [((width / 2), (height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = red

    def get_head_position(self):
        return self.position[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * grid_size)) % width), (cur[1] + (y * grid_size)) % height)
        if len(self.position) > 2 and new in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0, new)
            if len(self.position) > self.length:
                self.position.pop()

    def reset(self):
        self.length = 1
        self.position = [((width / 2), (height / 2))]
        self.direction = random.choice([up, down, left, right])

    def draw(self, surface):
        for p in self.position:
            r = pygame.Rect((p[0], p[1]), (grid_size, grid_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, white, r, 1)

    def collide(self, x, y):
        if x < 0 or x >= width or y < 0 or y >= height:
            return True
        for p in self.position[1:]:
            if x == p[0] and y == p[1]:
                return True
        return False

class Food:
    def __init__(self, level_data):
        self.position = (0, 0)
        self.color = white
        self.timer = 500  # timer value
        self.level_data = level_data
        self.randomize_position()

    def randomize_position(self):
        # Generate random position for food, within the playable area defined by the level data
        while True:
            x = random.randint(0, len(self.level_data[0]) - 1) * grid_size
            y = random.randint(0, len(self.level_data) - 1) * grid_size
            if self.level_data[y // grid_size][x // grid_size] == ' ':
                self.position = (x, y)
                break

    def update_timer(self):
        # Decrease timer value
        self.timer -= 1
        if self.timer == 0:
            self.randomize_position()
            self.timer = 500  # Reset timer value

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, r)

def load_level(filename):
    # Load level data from the text file
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def main():
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('snake')

    clock = pygame.time.Clock()

    snake = Snake()

    # Load level data
    level_data = load_level('level1.txt')

    # Create food object with level data
    food = Food(level_data)

    running = True
    score = 0
    level = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(up)
                elif event.key == pygame.K_DOWN:
                    snake.turn(down)
                elif event.key == pygame.K_LEFT:
                    snake.turn(left)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(right)

        snake.move()
        food.update_timer()
        if snake.collide(food.position[0], food.position[1]):
            score += 1
            if score % 3 == 0:
                level += 1
            snake.length += 1
            food.randomize_position()

        window.fill(black)
        snake.draw(window)
        food.draw(window)
        pygame.display.flip()

        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()
