import pygame
import random

# Required to initalize pygame.
pygame.init()

# Created Python game window (takes width and height).
screen = pygame.display.set_mode((700, 700))

# Added a backgound image to replace screen.fill solution.
background_image = pygame.image.load('Pygame_Practice_Background.png')

# Added Title
pygame.display.set_caption("Space Wars")

# Add the player image.
player_image = pygame.image.load('Pygame_Practice_Player.png')
player_location_x = 325
player_location_y = 600
player_x_change = 0
player_y_change = 0

# Added player bullet.
player_bullet_image = pygame.image.load('Pygame_Practice_Player_Bullet.png')
player_bullet_location_x = 0
# How can I make this location equal to the location of the player????
player_bullet_location_y = 600
player_bullet_change = 10
player_bullet_state = "ready"

# Add the enemy image.
enemy_image = pygame.image.load('Pygame_Practice_Enemy.png')
enemy_location_x = random.randint(0, 700)
enemy_location_y = random.randint(0, 325)
enemy_x_change = 4
enemy_y_change = 4

# Added player function that uses the blit method to put the player image on the game screen.
def player(x, y):
    screen.blit(player_image, (x, y))

# Added global to allow the function to be called from inside this function.
def fire_bullet(x, y):
    global player_bullet_state
    player_bullet_state = "fire"
    screen.blit(player_bullet_image, (x + 16, y + 10))

# Added player function that uses the blit method to put the player image on the game screen.
def enemy(x, y):
    screen.blit(enemy_image, (x, y))

# Game Loop: While loop used to keep the game window open until user closes.
running = True
while running:

    # Alternative Solution: screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Added keystroke events to allow the user to control the game play.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -4
            if event.key == pygame.K_RIGHT:
                player_x_change = 4
            if event.key == pygame.K_UP:
                player_y_change = -4
            if event.key == pygame.K_DOWN:
                player_y_change = 4
            if event.key == pygame.K_SPACE:
                fire_bullet(player_location_x, player_bullet_location_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0


    player_location_x += player_x_change
    # This statement adds a boundary to are player to ensure it stays on the screen.
    if player_location_x <= 0:
        player_location_x = 0
    elif player_location_x >= 636:
        player_location_x = 636

    player_location_y += player_y_change
    if player_location_y <= 0:
        player_location_y = 0
    elif player_location_y >= 636:
        player_location_y = 636

    # Enemy movement.
    enemy_location_x += enemy_x_change

    if enemy_location_x <= 0:
        enemy_x_change = 4
        enemy_location_y += enemy_y_change
    elif enemy_location_x >= 636:
        enemy_x_change = -4
        enemy_location_y += enemy_y_change

    enemy_location_y += enemy_y_change
    if enemy_location_y <= 0:
        enemy_y_change = 2
        enemy_location_x += enemy_x_change
    elif enemy_location_y >= 636:
        enemy_y_change = -4
        enemy_location_x += enemy_x_change

    # Bullet movement.
    if player_bullet_state is "fire":
        fire_bullet(player_location_x, player_bullet_location_y)
        player_bullet_location_y -= player_bullet_change



    # This calls the player function and adds it to the game board.
    player(player_location_x, player_location_y)
    enemy(enemy_location_x, enemy_location_y)
    pygame.display.update()