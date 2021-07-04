import pygame, sys
from pygame.locals import *

from os import path

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animation = []
        self.animation.append(pygame.image.load(path.join('assets', 'animation_01.png')))
        self.animation.append(pygame.image.load(path.join('assets', 'animation_02.png')))
        self.animation.append(pygame.image.load(path.join('assets', 'animation_03.png')))
        self.animation.append(pygame.image.load(path.join('assets', 'animation_04.png')))
        self.animation.append(pygame.image.load(path.join('assets', 'animation_05.png')))
        self.animation.append(pygame.image.load(path.join('assets', 'animation_06.png')))
        self.current_sprite = 0
        self.image = self.animation[self.current_sprite]

        self.is_walking = False
        self.is_jumping = False

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


    def update(self):
        if self.is_jumping:
                for anime in range(5, 6):
                    self.current_sprite = anime
                    self.image = self.animation[int(self.current_sprite)]
                self.is_jumping = False

        if self.is_walking:
            self.current_sprite += 0.2
            if self.current_sprite >= 5 or self.is_walking == False:
                self.current_sprite = 0
            self.image = self.animation[int(self.current_sprite)]
        
        
        


pygame.init()
screen_width = 400
screen_height = 400


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("mario_animation")


moving_sprites = pygame.sprite.Group()
player = Player(-40, -40)
moving_sprites.add(player)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player.is_walking = True
            elif event.key == K_SPACE:
                player.is_jumping = True
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                player.is_walking = False


    screen.fill((0, 0, 0))
    moving_sprites.update()
    moving_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)