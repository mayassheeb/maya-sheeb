import pygame
import sys
import time
from pygame.locals import* 
pygame.init()
pygame.display.set_caption("Basics")

screen=pygame.display.set_mode((600,400))
BLACK = (0,0,0)
WHITE= (255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)

while True:
	pygame.draw.rect(screen,WHITE,(0,50,30,70))
	pygame.display.update()
	time.sleep(0.001)