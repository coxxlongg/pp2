import psycopg2
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Database connection
conn = psycopg2.connect(database="YourDatabase", 
                        user="YourUsername", 
                        password="YourPassword", 
                        host="localhost", 
                        port="5432")

# Define User and User_Score tables
create_tables_query = """
CREATE TABLE IF NOT EXISTS "User" (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS user_score (
    score_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "User"(user_id),
    level INT NOT NULL,
    score INT NOT NULL
);
"""

# Function to create tables if they don't exist
def create_tables():
    cur = conn.cursor()
    cur.execute(create_tables_query)
    conn.commit()
    cur.close()

# Function to prompt user for username
def get_username():
    return input("Enter your username: ")

# Function to check if user exists
def user_exists(username):
    cur = conn.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM \"User\" WHERE username = %s)", (username,))
    return cur.fetchone()[0]

# Function to display user's current level
def show_current_level(username):
    cur = conn.cursor()
    cur.execute("""
        SELECT level FROM user_score 
        INNER JOIN "User" ON user_score.user_id = "User".user_id 
        WHERE "User".username = %s
        ORDER BY score_id DESC
        LIMIT 1
    """, (username,))
    row = cur.fetchone()
    if row:
        print(f"Welcome back, {username}! Your current level is: {row[0]}")
    else:
        print(f"Welcome, {username}!")

# Function to insert user's score into the database
def insert_user_score(user_id, level, score):
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()

# Function to handle keyboard events
def handle_events(username, level, score):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                # Pause the game and save score to database
                insert_user_score(get_user_id(username), level, score)
                print("Game paused. Score saved.")
                time.sleep(1)  # Prevent multiple key presses
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()

# Function to get user ID
def get_user_id(username):
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM \"User\" WHERE username = %s", (username,))
    return cur.fetchone()[0]

# Main game loop
def game_loop(username):
    
pygame.init()

# colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# size
display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
initial_snake_speed = 15
level_speed_increment = 3
initial_food_timer = 200
level_food_timer_decrement = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [[display_width / 2, display_height / 2]]
        self.direction = 'STOP'
        self.color = black

    def move(self):
        if self.direction == 'UP':
            new_head = [self.positions[0][0], self.positions[0][1] - snake_block]
        elif self.direction == 'DOWN':
            new_head = [self.positions[0][0], self.positions[0][1] + snake_block]
        elif self.direction == 'LEFT':
            new_head = [self.positions[0][0] - snake_block, self.positions[0][1]]
        elif self.direction == 'RIGHT':
            new_head = [self.positions[0][0] + snake_block, self.positions[0][1]]
        else:
            return

        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for position in self.positions:
            pygame.draw.rect(surface, self.color, [position[0], position[1], snake_block, snake_block])

    def eat(self):
        self.length += 1


class Food:
    def __init__(self):
        self.position = [random.randrange(1, (display_width // snake_block)) * snake_block,
                         random.randrange(1, (display_height // snake_block)) * snake_block]
        self.color = green
        self.timer = initial_food_timer

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.position[0], self.position[1], snake_block, snake_block])

    def respawn(self):
        self.position = [random.randrange(1, (display_width // snake_block)) * snake_block,
                         random.randrange(1, (display_height // snake_block)) * snake_block]
        self.timer = initial_food_timer

    def update_timer(self):
        self.timer -= 1
        if self.timer == 0:
            self.respawn()


def show_score(score, level):
    score_text = score_font.render("Score: " + str(score), True, yellow)
    level_text = score_font.render("Level: " + str(level), True, yellow)
    dis.blit(score_text, [0, 0])
    dis.blit(level_text, [0, 40])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])


def generate_weighted_food():
    # Define food types and their respective weights
    food_types = ['normal', 'special']
    weights = [0.8, 0.2]  # Normal food 80%, Special food 20%

    # Randomly select a food type based on weights
    return random.choices(food_types, weights)[0]


def game_loop():
    game_over = False
    game_close = False
    level = 1
    snake_speed = initial_snake_speed
    score = 0

    snake = Snake()
    food = Food()

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You lost! Press Q-Quit or C-Play Again", red)
            show_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'
                elif event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'

        snake.move()
        food.update_timer()

        # Check for collision with food
        if snake.positions[0] == food.position:
            if generate_weighted_food() == 'normal':
                snake.eat()
                score += 1
            else:
                # Special food increases score and length more than normal food
                snake.eat()
                snake.eat()
                score += 2

            food.respawn()

            # Check if level should increase based on score
            if score % 3 == 0:
                level += 1
                snake_speed += level_speed_increment
                food.timer -= level_food_timer_decrement

        # Check for collision with walls or self
        if (snake.positions[0][0] >= display_width or snake.positions[0][0] < 0 or
                snake.positions[0][1] >= display_height or snake.positions[0][1] < 0):
            game_close = True
        for block in snake.positions[1:]:
            if snake.positions[0] == block:
                game_close = True

        dis.fill(blue)
        snake.draw(dis)
        food.draw(dis)
        show_score(score, level)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


    pass

# Main function
def main():
    create_tables()

    username = get_username()
    if user_exists(username):
        show_current_level(username)
    else:
        print("New user! Welcome!")

    # Start the game loop
    game_loop(username)

    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()
