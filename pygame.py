import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake block size and speed
BLOCK_SIZE = 10
SNAKE_SPEED = 15

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock
clock = pygame.time.Clock()

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    """Display the player's score."""
    value = score_font.render("Your Score: " + str(score), True, BLUE)
    screen.blit(value, [0, 0])

def our_snake(block_size, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], block_size, block_size])

def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def place_food(snake_list):
    """Place food on the screen, ensuring it does not overlap with the snake."""
    while True:
        foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
        foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
        if [foodx, foody] not in snake_list:
            return foodx, foody

def gameLoop():
    """Main game loop."""
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx, foody = place_food(snake_list)

    while not game_over:

        while game_close:
            screen.fill(WHITE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Restart the game without recursion
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(BLOCK_SIZE, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = place_food(snake_list)
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

gameLoop()