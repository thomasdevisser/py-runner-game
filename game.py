import pygame
from sys import exit

pygame.init()

# Create the display and time
pygame.display.set_caption('PyRunner')
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
game_active = True

# The text
font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_state = font.render('Dodge the snails!', False, 'black')
game_state_rect = game_state.get_rect(midtop=(400, 50))
score = 0
score_display = font.render("{}".format(score), False, 'black')
score_display_rect = score_display.get_rect(topleft=(50, 50))

# The scene
sky = pygame.image.load('graphics/sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

# The player
player = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(100, 300))
player_gravity = 0  # The gravity grows the longer you fall to fake physics

# The snail
snail = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom=(600, 300))

while True:
    # Loop through all the events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # Jump if you click the player
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(pygame.mouse.get_pos()):
            #         player_gravity = -20

            # Check for keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # You can only jump if you're on the ground
                    if player_rect.bottom == 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                snail_rect = snail.get_rect(midbottom=(600, 300))
                player_rect = player.get_rect(midbottom=(100, 300))
                game_state = font.render('Dodge the snails!', False, 'black')
                game_state_rect = game_state.get_rect(midtop=(400, 50))
                score = 0
                game_active = True

    if game_active:
        # Render all the visuals to the screen
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))
        screen.blit(game_state, game_state_rect)
        screen.blit(score_display, score_display_rect)
        screen.blit(snail, snail_rect)
        screen.blit(player, player_rect)

        # Move the characters
        snail_rect.left -= 6

        player_gravity += 1
        player_rect.y += player_gravity

        # Make it look like the player is standing
        if player_rect.bottom > 300:
            player_rect.bottom = 300

        # Handle graphics going off-screen
        if snail_rect.left < -100:
            snail_rect.left = 900
            score += 1
            score_display = font.render("{}".format(score), False, 'black')
            screen.blit(score_display, score_display_rect)

        # Check for rectangles colliding
        if player_rect.colliderect(snail_rect):
            print("BOOM, snail hits the player")
            game_active = False

        # Check for mouse colliding
        # mouse = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse):
        #     print("mouse on player")

        # Check for keys being pressed
        # keys_pressed = pygame.key.get_pressed()
        # if keys_pressed[pygame.K_SPACE]:
        #     print('JUMP')

        # Rerender the display
        pygame.display.update()

        # Set the framerate to a max of 60fps
        clock.tick(60)
    else:
        screen.fill("black")
        game_state = font.render('Game Over', False, 'white')
        game_state_rect = game_state.get_rect(midtop=(400, 50))
        screen.blit(game_state, game_state_rect)

        # Rerender the display
        pygame.display.update()
