import pygame
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/fly_1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly_2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            self.index = 0
            y_pos = 210
        else:
            snail_1 = pygame.image.load(
                'graphics/snail/snail_1.png').convert_alpha()
            snail_2 = pygame.image.load(
                'graphics/snail/snail_2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            self.index = 0
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def update(self):
        self.animate()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def animate(self):
        self.index += 0.1
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]
