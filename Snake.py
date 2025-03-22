import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Define display dimensions
DIS_WIDTH = 800
DIS_HEIGHT = 600

# Define snake block size and speed
SNAKE_BLOCK = 20
SNAKE_SPEED = 5

# Set up the display
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Fonts for displaying score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [[DIS_WIDTH // 2, DIS_HEIGHT // 2]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def move(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        x, y = self.positions[0]
        if self.direction == 'UP':
            y -= SNAKE_BLOCK
        if self.direction == 'DOWN':
            y += SNAKE_BLOCK
        if self.direction == 'LEFT':
            x -= SNAKE_BLOCK
        if self.direction == 'RIGHT':
            x += SNAKE_BLOCK

        self.positions.insert(0, [x, y])

        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, GREEN, [pos[0], pos[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def check_collision(self):
        x, y = self.positions[0]
        if x >= DIS_WIDTH or x < 0 or y >= DIS_HEIGHT or y < 0:
            return True
        for block in self.positions[1:]:
            if x == block[0] and y == block[1]:
                return True
        return False

    def increase_length(self):
        self.length += 1

class Apple:
    def __init__(self):
        self.position = [random.randrange(1, (DIS_WIDTH // SNAKE_BLOCK)) * SNAKE_BLOCK,
                         random.randrange(1, (DIS_HEIGHT // SNAKE_BLOCK)) * SNAKE_BLOCK]

    def draw(self, surface):
        pygame.draw.rect(surface, RED, [self.position[0], self.position[1], SNAKE_BLOCK, SNAKE_BLOCK])

def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    snake = Snake()
    apple = Apple()

    while not game_over:

        while game_close:
            dis.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            show_score(snake.length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    snake.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    snake.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    snake.change_to = 'RIGHT'

        snake.move()

        if snake.check_collision():
            game_close = True

        if snake.positions[0] == apple.position:
            snake.increase_length()
            apple = Apple()

        dis.fill(BLACK)
        snake.draw(dis)
        apple.draw(dis)
        show_score(snake.length - 1)

        pygame.display.update()

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

gameLoop()