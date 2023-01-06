import pygame
from sys import exit

pygame.init()

# Create the display and time
pygame.display.set_caption('PyRunner')
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

night_sky = pygame.image.load('assets/night-sky.png')
night_ground = pygame.image.load('assets/night-ground.png')

snail = pygame.image.load('assets/snail-in-moonlight.png')
snail_position_x = 600

title_surface = font.render('PyRunner', False, '#babec2')

while True:
    # Loop through all the events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Add the background surfaces
    screen.blit(night_sky, (0, 0))
    screen.blit(night_ground, (0, 290))

    screen.blit(title_surface, (50, 50))

    screen.blit(snail, (snail_position_x, 249))
    snail_position_x -= 2

    # Rerender the display
    pygame.display.update()

    # Set the framerate to a max of 60fps
    clock.tick(60)
