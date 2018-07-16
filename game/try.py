import pygame
import random
from os import path

img_dir = path.join(path.dirname(file), 'img')
snd_dir = path.join(path.dirname(file),'music')

font_name = pygame.font.match_font('comic sans')
def draw_text(surf, text, size, x, y):
font = pygame.font.Font(font_name, size)
text_surface = font.render(text, True, WHITE)
text_rect = text_surface.get_rect()
text_rect.midtop = (x,y)
surf.blit(text_surface, text_rect)

WIDTH = 480
HEIGHT = 600
FPS = 60