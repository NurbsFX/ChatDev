'''
This is the main file of the snake game.
'''
import pygame
import sys
import time
import random
# Initialize the game
pygame.init()
# Set up the display
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
# Set up the game clock
clock = pygame.time.Clock()
# Set up the snake and food
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawn = True
direction = "RIGHT"
change_to = direction
score = 0
# Game over function
def game_over():
    font_style = pygame.font.SysFont(None, 50)
    message = font_style.render("Game Over!", True, red)
    message_rect = message.get_rect()
    message_rect.center = (width / 2, height / 2)
    display.blit(message, message_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = "LEFT"
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = "DOWN"
    # Validate the direction
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    # Update the snake position
    if direction == "RIGHT":
        snake_position[0] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    # Spawn food
    if not food_spawn:
        food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawn = True
    # Draw the snake and food
    display.fill(black)
    for pos in snake_body:
        pygame.draw.rect(display, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(display, white, pygame.Rect(food_position[0], food_position[1], 10, 10))
    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > width - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > height - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    # Update the display
    pygame.display.update()
    clock.tick(15)