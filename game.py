import pygame
from sys import exit

pygame.init()

# Create the display and time
pygame.display.set_caption('PyRunner')
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

night_sky = pygame.image.load('assets/night-sky.png')
night_ground = pygame.image.load('assets/night-ground.png')

while True:
    # Loop through all the events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(night_sky, (0, 0))
    screen.blit(night_ground, (0, 290))

    # Rerender the display
    pygame.display.update()

    # Set the framerate to a max of 60fps
    clock.tick(60)
