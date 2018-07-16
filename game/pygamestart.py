import pygame
import sys
import time
from pygame.locals import* 
pygame.init()
pygame.display.set_caption("Basics")
direction="forward"
x=160
screen=pygame.display.set_mode((500,400))
BLACK = (0,0,0)
WHITE= (255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)

pygame.draw.rect(screen,WHITE,(x,100,100,50))

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(BLACK)
	if(direction=="forward"):
		x=x+5
		if (x>=400):
			direction="backward"
	elif(direction == "backward"):
		x= x-5
		if (x<=0):
			direction="forward"
	pygame.draw.rect(screen,WHITE,(x,100,100,50))
	pygame.display.update()
	time.sleep(0.001)
	
