import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
SNAKE_SIZE = 20
SNAKE_SPEED = 20

# Set up some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Snake:
    def __init__(self):
        self.body = [[100, 50], [80, 50], [60, 50]]
        self.direction = 'RIGHT'

    def change_direction(self, dir):
        self.direction = dir

    def move(self):
        head = self.body[0].copy()
        if self.direction == 'RIGHT':
            head[0] += SNAKE_SPEED
        elif self.direction == 'LEFT':
            head[0] -= SNAKE_SPEED
        elif self.direction == 'UP':
            head[1] -= SNAKE_SPEED
        elif self.direction == 'DOWN':
            head[1] += SNAKE_SPEED
        self.body.insert(0, head)
        self.body.pop()

    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(part[0], part[1], SNAKE_SIZE, SNAKE_SIZE))

snake = Snake()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.change_direction('RIGHT')

    snake.move()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the snake
    snake.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the framerate
    pygame.time.Clock().tick(60)
