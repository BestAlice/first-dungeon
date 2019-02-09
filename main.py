import pygame
import os
from permanent import WIDTH, HEIGHT, FPS
#плохо работает слейдующая строчка
from Camera import Camera

from fire_magician import Fire_magician
from goblin import Goblin

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

all_sprites = pygame.sprite.Group()
player = Fire_magician(all_sprites)

gobs = Goblin(all_sprites)
gobs.Fire_x_y(player, player.rect)

screen.fill(pygame.Color('black')) #почему бы и нет

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('black'))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

