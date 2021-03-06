# coding: utf-8
import pygame
import os
WIDTH = 1000 #ширина
HEIGHT = 700 #высота
FPS = 30

#границы для справки
LEFT = 100
RIGHT = 860
UP = 0
DOWN = 540

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image

def load_music(name):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()                 
    pygame.mixer.music.set_volume(0.1)

def draw(screen, text, x, y, color='white', size=50):
    font = pygame.font.Font("data/Font.ttf", size)
    text = font.render(text, 1, pygame.Color(color))
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (x, y))