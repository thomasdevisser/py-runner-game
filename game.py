import pygame
from sys import exit
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load(
            'graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load(
            'graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(
            'graphics/player/player_jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(200, 300))
        self.gravity = 0

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate()

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300 and self.rect.bottom > 100:
            self.gravity = -15

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom > 300:
            self.rect.bottom = 300

    def animate(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]


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

player = pygame.sprite.GroupSingle()
player.add(Player())

# The scene
sky = pygame.image.load('graphics/sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

# Player on game inactive
player_stand = pygame.image.load(
    'graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# The snail
snail_1 = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()
snail_2 = pygame.image.load('graphics/snail/snail_2.png').convert_alpha()
snail_list = [snail_1, snail_2]
snail_index = 0
snail = snail_list[snail_index]

# The fly
fly_1 = pygame.image.load('graphics/fly/fly_1.png').convert_alpha()
fly_2 = pygame.image.load('graphics/fly/fly_2.png').convert_alpha()
fly_list = [fly_1, fly_2]
fly_index = 0
fly = fly_list[fly_index]

# Enemies
enemy_rect_list = []

# Making a custom event
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, randint(1200, 1400))

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    # Loop through all the events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == enemy_timer:
                if randint(0, 2):
                    enemy_rect_list.append(snail.get_rect(
                        midbottom=(randint(900, 1200), 300)))
                else:
                    enemy_rect_list.append(fly.get_rect(
                        midbottom=(randint(900, 1200), 200)))

            if event.type == snail_animation_timer:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0
                snail = snail_list[snail_index]

            if event.type == fly_animation_timer:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0
                fly = fly_list[fly_index]
        else:
            if event.type == pygame.KEYDOWN:
                start_score = int(pygame.time.get_ticks() / 100)
                enemy_rect_list.clear()
                game_active = True

    if game_active:
        # Render all the visuals to the screen
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))

        player.draw(screen)
        player.update()

        enemy_rect_list = spawn_enemies(enemy_rect_list)

        display_game_state("Don't get hit!")
        score = display_score()

        # game_active = check_collision(player_rect, enemy_rect_list)
    else:
        screen.fill("#cdf2f5")
        screen.blit(player_stand, player_stand_rect)
        display_game_state("Game over!")
        display_final_score(score)

    # Rerender the display
    pygame.display.update()

    # Set the framerate to a max of 60fps
    clock.tick(60)
