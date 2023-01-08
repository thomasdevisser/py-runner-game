import pygame
from sys import exit
from random import randint


def display_score():
    score = int(pygame.time.get_ticks() / 100) - start_score
    score_display = font.render(f"{score}", False, 'black')
    score_display_rect = score_display.get_rect(topleft=(50, 50))
    screen.blit(score_display, score_display_rect)
    return score


def display_final_score(score):
    score_display = font.render(f"You scored {score}", False, 'black')
    score_display_rect = score_display.get_rect(center=(400, 350))
    screen.blit(score_display, score_display_rect)


def display_game_state(state_text):
    game_state = font.render(state_text, False, 'black')
    game_state_rect = game_state.get_rect(midtop=(400, 50))
    screen.blit(game_state, game_state_rect)


def spawn_enemies(enemy_rect_list):
    if enemy_rect_list:
        for enemy_rect in enemy_rect_list:
            enemy_rect.x -= randint(4, 5)

            if enemy_rect.bottom == 300:
                screen.blit(snail, enemy_rect)
            else:
                screen.blit(fly, enemy_rect)

        enemy_rect_list = [
            enemy for enemy in enemy_rect_list if enemy.x > -100]

    return enemy_rect_list


def check_collision(player, enemies):
    if enemies:
        for enemy in enemy_rect_list:
            if player.colliderect(enemy):
                return False
    return True


def player_animation():
    global player, player_index

    if player_rect.bottom < 300:
        player = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player = player_walk[int(player_index)]


pygame.init()

# Create the display and time
pygame.display.set_caption('PyRunner')
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
game_active = True

# The text
font = pygame.font.Font('font/Pixeltype.ttf', 50)

start_score = 0
score = 0
player_gravity = 0  # The gravity grows the longer you fall to fake physics

# The scene
sky = pygame.image.load('graphics/sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

# The player
player_walk_1 = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load(
    'graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]

player_index = 0

player_jump = pygame.image.load(
    'graphics/player/player_jump.png').convert_alpha()

player = player_walk[player_index]
player_rect = player.get_rect(midbottom=(100, 300))

# Player on game inactive
player_stand = pygame.image.load(
    'graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# The snail
snail = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()

# The fly
fly = pygame.image.load('graphics/fly/fly_1.png').convert_alpha()

# Enemies
enemy_rect_list = []

# Making a custom event
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, randint(1200, 1400))

while True:
    # Loop through all the events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # Check for keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # You can only jump if you're on the ground
                    print(player_rect.bottom)
                    if player_rect.bottom <= 300 and player_rect.bottom > 100:
                        player_gravity = -15

            if event.type == enemy_timer:
                if randint(0, 2):
                    enemy_rect_list.append(snail.get_rect(
                        midbottom=(randint(900, 1200), 300)))
                else:
                    enemy_rect_list.append(fly.get_rect(
                        midbottom=(randint(900, 1200), 200)))
        else:
            if event.type == pygame.KEYDOWN:
                start_score = int(pygame.time.get_ticks() / 100)
                enemy_rect_list.clear()
                game_active = True

    if game_active:
        # Render all the visuals to the screen
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))

        player_animation()
        screen.blit(player, player_rect)

        enemy_rect_list = spawn_enemies(enemy_rect_list)

        display_game_state("Don't get hit!")
        score = display_score()

        player_gravity += 1
        player_rect.y += player_gravity

        # Make it look like the player is standing
        if player_rect.bottom > 300:
            player_rect.bottom = 300

        game_active = check_collision(player_rect, enemy_rect_list)
    else:
        screen.fill("#cdf2f5")
        screen.blit(player_stand, player_stand_rect)
        display_game_state("Game over!")
        display_final_score(score)

    # Rerender the display
    pygame.display.update()

    # Set the framerate to a max of 60fps
    clock.tick(60)
