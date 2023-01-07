import pygame
from sys import exit

pygame.init()

# Create the display and time
pygame.display.set_caption('PyRunner')
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# The title
font = pygame.font.Font('font/Pixeltype.ttf', 50)
title = font.render('Escaping Cindy', False, 'black')
title_rect = title.get_rect(center=(400, 50))

# The scene
sky = pygame.image.load('graphics/sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

# The player
player = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(100, 300))
player_walking_left = False
player_walking_right = False

# The snail
snail = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom=(600, 300))

while True:
    # Loop through all the events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("JUMP")

            if event.key == pygame.K_d:
                print("WALK RIGHT")
                player_walking_right = True

            if event.key == pygame.K_a:
                print("WALK LEFT")
                player_walking_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_walking_right = False

            if event.key == pygame.K_a:
                player_walking_left = False

    # Render all the visuals to the screen
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(title, title_rect)
    screen.blit(snail, snail_rect)
    screen.blit(player, player_rect)

    # Move the characters
    snail_rect.left -= 2

    if player_walking_right:
        player_rect.right += 2

    if player_walking_left:
        player_rect.left -= 2

    # Handle graphics going off-screen
    if snail_rect.left < -100:
        snail_rect.left = 900

    # Check for rectangles colliding
    if player_rect.colliderect(snail_rect):
        print("BOOM, snail hits the player")

    # Check for mouse colliding
    mouse = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse):
        print("mouse on player")

    # Check for keys being pressed
    # keys_pressed = pygame.key.get_pressed()
    # if keys_pressed[pygame.K_SPACE]:
    #     print('JUMP')

    # Rerender the display
    pygame.display.update()

    # Set the framerate to a max of 60fps
    clock.tick(60)
