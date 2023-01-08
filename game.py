import pygame
from random import randint, choice
from sys import exit
from classes.Player import Player
from classes.Enemy import Enemy


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


def collision_sprites():
    if pygame.sprite.spritecollide(player.sprite, enemies, False):
        return False
    else:
        return True


pygame.init()

# The scene
pygame.display.set_caption('PyRunner')
screen = pygame.display.set_mode((800, 400))
sky = pygame.image.load('graphics/sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

# Create the general game settings
soundtrack = pygame.mixer.Sound('audio/music.wav')
soundtrack.set_volume(0.2)
soundtrack.play(loops=-1)
font = pygame.font.Font('font/Pixeltype.ttf', 50)
clock = pygame.time.Clock()
game_active = True
start_score = 0
score = 0

# Groups
enemies = pygame.sprite.Group()
player = pygame.sprite.GroupSingle()

player.add(Player())

# Player on game inactive
player_stand = pygame.image.load(
    'graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Custom events
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, randint(1200, 1400))

while True:
    # Loop through all the events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == enemy_timer:
                enemies.add(Enemy(choice(['snail', 'snail', 'snail', 'fly'])))
        else:
            if event.type == pygame.KEYDOWN:
                enemies.empty()
                start_score = int(pygame.time.get_ticks() / 100)
                game_active = True

    # Render all the visuals to the screen
    if game_active:
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))

        player.draw(screen)
        player.update()

        enemies.draw(screen)
        enemies.update()

        display_game_state("Don't get hit!")
        score = display_score()

        game_active = collision_sprites()
    else:
        screen.fill("#cdf2f5")
        screen.blit(player_stand, player_stand_rect)
        display_game_state("Game over!")
        display_final_score(score)

    # Rerender the display
    pygame.display.update()

    # Set the framerate to a max of 60fps
    clock.tick(60)
