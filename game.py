import pygame
from sys import exit

pygame.init()

# Create the display and time
pygame.display.set_caption('PyRunner')
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky = pygame.image.load('graphics/sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

snail = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom=(600, 300))

player = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(100, 300))

title_surface = font.render('PyRunner', False, 'black')

while True:
    # Loop through all the events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Add the background surfaces
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))

    screen.blit(title_surface, (50, 50))

    screen.blit(snail, snail_rect)
    screen.blit(player, player_rect)

    snail_rect.left -= 2
    if snail_rect.left < -100:
        snail_rect.left = 900

    # Rerender the display
    pygame.display.update()

    # Set the framerate to a max of 60fps
    clock.tick(60)
