import pygame
import sys
import time
from pygame.locals import * 
pygame.init()
pygame.display.set_caption("Basics")
direction="forward"
ydirection="upward"
x=100
y=90
screen=pygame.display.set_mode((500,400))
BLACK = (0,0,0)
WHITE= (255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
PINK=(255,90,217)
pygame.draw.circle(screen, PINK, (x,y),70,0)

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
			if(ydirection=="upward"):
					y = y - 5
				if(y<=70):
					ydirection = "downward"
				elif(ydirection=="downward"):
					y=y+7
					if (y>=330):
						ydirection="upward"
				if(direction=="forward"):
					x=x+6
					if(x>=430):
						direction="backward"
					elif(direction=="backward"):
						x=x-7
						if(x<=70):
							direction="forward"
	screen.fill(BLACK)
	pygame.draw.circle(screen, PINK, (x,y),70,0)
	pygame.display.update()
	time.sleep(0.01)