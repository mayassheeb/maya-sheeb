import pygame
import sys
import time
from pygame.locals import *
import random 
from random import randint
import pygame
import sys
import time
from pygame.locals import *

#colors
BLUE = (132, 237, 245)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE= (235, 29, 235)
PINK=(255,90,217)
LIGHTPINK = (245, 192 , 220)
LIGHTBLUE = (196, 224, 243)
P = (191, 51, 139)
L = (253, 149, 215)
UNICORN_SIZE = 140
color = PINK 

#screen setup 
pygame.init()
pygame.display.set_caption("basic")
screen = pygame.display.set_mode((1300, 500))
screen_width = 1300
screen_number = 1
screen_height = 500

ystart = 500
xstart = 60
#unicorn (x,y)
x = xstart
y = ystart

y_velocity = 0
x_velocity = 0 

jump = False
jump_height = 10
speed = 0

game_score=0



# keep track of x and y position of mario
def draw_blocks(block_x , block_y , heigth, width,color):
	return pygame.draw.rect(screen,color,(block_x, block_y, heigth, width))

def unicorn_not_on_platform(x, y):
	unicorn_x = x + UNICORN_SIZE/2
	unicorn_y = y + UNICORN_SIZE
	for block in blocks:
		block_x = block[0]
		block_width = block[2]
		block_y = block[1]
		if unicorn_x >= block_x and unicorn_x <= (block_x + block_width):
			if unicorn_y >= block_y:
				unicorn_y = block_y - 40
				return unicorn_y
	unicorn_y = 500
	return unicorn_y
def score():
	myfont = pygame.font.SysFont("monospace", 100)
	label = myfont.render(str(game_score),1,BLACK)
	screen.blit(label, (20, 30))


#draw mario
# def draw_mario():
# Game loop
pygame.mixer.music.load('alne1.mp3')
pygame.mixer.music.play(10)

from sys import exit
pink = pygame.image.load('1234.bmp')      
screen.blit(pink ,(0,0)) 
pygame.display.flip()
img = pygame.image.load("unicorn.png")


blocks = []

# y = unicorn_not_on_platform(x,y)
# y_start = y
# print y

while True:
	pink = pygame.image.load ('1234.bmp')
	screen.fill((0,0,0))
	pink = pygame.transform. scale(pink, (1300, 500))
	screen.blit(pink,(0,0))
	# Draw mario
	# pygame.draw.rect(screen, BLUE, (x, y, 40, 40))
	# background = pygame.transform.scale (img2, (BACKGROUND_SIZE , BACKGROUND_SIZE))
	# screen.blit( background, (1300,500 ))
	
	if (x >= screen_width - 40):
		screen_number = (screen_number+1) % 3
		x = 5
		print screen_number

	blocks = []
	if screen_number == 1:

		blocks.append(draw_blocks(0, 420 , 170 , 1000 , PURPLE))
		blocks.append(draw_blocks(250, 420,170, 1000, PURPLE))
		blocks.append(draw_blocks(400, 360, 120, 1000, PURPLE))
		blocks.append(draw_blocks(600, 360, 100, 500, PURPLE))
		blocks.append(draw_blocks(700, 300, 120, 2000, PURPLE))
		blocks.append(draw_blocks(820, 420, 180, 1000, PURPLE))
		blocks.append(draw_blocks(1100, 300, 200, 10, L))


	elif screen_number == 2:
		blocks.append(draw_blocks(0, 250, 180, 10, L))
		blocks.append(draw_blocks(230, 350, 180, 10, L))
		blocks.append(draw_blocks(530, 420, 250, 100, PURPLE))
		blocks.append(draw_blocks(780, 360, 100, 30, L))
		blocks.append(draw_blocks(895, 420, 100, 100, PURPLE))
		blocks.append(draw_blocks(1000, 370, 80, 30, L))
		blocks.append(draw_blocks(1200, 340, 80, 30, L))

	elif screen_number == 0:
		blocks.append(draw_blocks(0, 320, 60, 30, L))
		blocks.append(draw_blocks(90, 400, 80, 20, L))
		blocks.append(draw_blocks(210, 450, 350, 100, PURPLE))
		blocks.append(draw_blocks(590, 360, 100, 50, L))
		blocks.append(draw_blocks(710, 300, 200, 50, L))
		blocks.append(draw_blocks(950, 450, 220, 100, PURPLE))
		blocks.append(draw_blocks(1170, 350, 130, 300, PURPLE)) 
	speed = speed - 4
	y = y - speed
	y_start = unicorn_not_on_platform(x,y)
	if y >= y_start:
		y = y_start
		speed = 3
	unicorn = pygame.transform.scale(img, ( UNICORN_SIZE , UNICORN_SIZE))
	screen.blit(unicorn, (x,y - 100))
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_RIGHT:
				x = x + 100
			if event.key == pygame.K_SPACE:
				speed = speed + 10
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	

	

	#jumpin logic 

	
	
	if keys[pygame.K_RIGHT]:
		game_score+=1
	score()
	if (y <= 0):
		y = 100
	if (y == 500):
		# print "GAME OVER"
		from sys import exit
		GO2 = pygame.image.load('GO2.bmp')      
		screen.blit(GO2 ,(0,0))
		game_over = pygame.image.load ('GO2.bmp')
		screen.fill((255,255,255))
		game_over = pygame.transform. scale(game_over, (1300, 500))
		screen.blit(GO2,(0,0)) 
	
	pygame.display.update()
	time.sleep(0.1)
