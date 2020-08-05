import pygame

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

# Added player function that uses the blit method to put the player image on the game screen.
def player(x, y):
    screen.blit(player_image, (x, y))

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0


    player_location_x += player_x_change
    player_location_y += player_y_change
    # This calls the player function and adds it to the game board.
    player(player_location_x, player_location_y)
    pygame.display.update()