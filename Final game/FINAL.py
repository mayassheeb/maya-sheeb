import pygame
import sys
import time
from pygame.locals import *

# Define Constant Variables

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE= (235, 29, 235)
color = PURPLE
# Setup Screen

pygame.init()

pygame.display.set_caption("basic")
screen = pygame.display.set_mode((2000, 500))
def draw_blocks(block_x , block_y , heigth, width,color):
	pygame.draw.rect(screen,color,(block_x, block_y, heigth, width))

# Define Variables

blocks=[]
draw_blocks((0, 420 , 170 , 1000 , PURPLE)-1)
draw_blocks((250, 420,170, 1000, PURPLE)-1)
draw_blocks((400, 360, 120, 1000, PURPLE)-1)
draw_blocks((600, 360, 100, 500, PURPLE)-1)
draw_blocks((700, 300, 120, 2000, PURPLE)-1)
draw_blocks((820, 420, 180, 1000, PURPLE)-1)
draw_blocks((1100, 300, 200, 10, WHITE)-1)
draw_blocks((1350, 250, 180, 10, WHITE)-1)
draw_blocks((1580, 350, 180, 10, WHITE)-1)
draw_blocks((1780, 420, 250, 100, PURPLE)-1)
draw_blocks((2080, 380, 40, 30, WHITE)-1)
draw_blocks((2150, 420, 30, 30, WHITE)-1)
draw_blocks((2230, 420, 180, 100, PURPLE)-1)
draw_blocks((2450, 370, 30, 30, WHITE)-1)
draw_blocks((2500, 340, 30, 30, WHITE)-1)
draw_blocks((2580, 320, 60, 30, WHITE)-1)
draw_blocks((2670, 400, 80, 20, WHITE)-1)
draw_blocks((2790, 450, 350, 100, PURPLE)-1)

# Game loop

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#### Update display

	pygame.display.update()

	time.sleep(0.001)