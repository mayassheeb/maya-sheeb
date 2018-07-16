import pygame
import sys
import time
from pygame.locals import *

# class player:
# 	def _init_(ball, x, y, size):
# 		ball.x = x
# 		ball.y = y 
# 		ball.size = size
# 		ball.jumping  = false
# 		ball.jump_offset = 0 
# 	def keys(player):
# 		keys = pygame.get_pressed()
# 		if keys[KEY_SPACE] and player.jumping == false and player.jump_offset == 0:
# 			player.jumping = True
# 	def do_jumping(player):
# 		global jump_height
# 		if player.jumping:
# 			player.jump_offset += 1
# 			if player.jump_offset >= jump_height:
# 				player.jumping = False
# 		elif player.jump_offset > 0 and player.jumping == False:
# 			player.jump_offset -=1
# 			dp_jumping(p)

# Define Constant Variables
BLUE = (132, 237, 245)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE= (235, 29, 235)
PINK=(255,90,217)
color = PURPLE
# Setup Screen

pygame.init()

pygame.display.set_caption("basic")
screen = pygame.display.set_mode((1300, 500))
screen_width = 500
screen_number = 1
radius = 40
length = 0 
mario_x = radius
mario_y = 380
y_velocity = 100
jump = False
y_position = 200
# time_in_air = 2
# p = player
jump_height = 20
mario = pygame.draw.circle(screen, BLUE, (mario_x, mario_y),radius,length)

 
# keep track of x and y position of mario
def draw_blocks(block_x , block_y , heigth, width,color):
	pygame.draw.rect(screen,color,(block_x, block_y, heigth, width))
#draw mario
# def draw_mario():



# Game loop

while True:

	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if event.type == pygame.KEYDOWN:
			if event.key == K_UP:
				jump = True
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	# keys(p)
	# do_jumping(p)
	# pygame.draw.circle(screen, BLUE, (p.x, p.y - p.jump_offset),radius,length)
	# platform_color = PINK
	# if p.jump_offset == 0:
	# 	platform_color = BLUE

	#if mario has hit the right side of the screen
		#screen_number = (screen_number + 1) % 3
		#update mario_x and mario_y
	if (mario_x>= screen_width-radius):
		screen_number = (screen_number+1) % 3
	# 	mario_x = radius
	# 	#y_position
	# 	#mario_x
	# if mario_y < 500:
	# 	time_in_air += 1
	# 	y_velocity = 1* time_in_air
	# 	#y_position
	# 	#mario_x 
	# elif mario_y == 500 - radius:
	# 	time_in_air=0

	if screen_number == 1:
		draw_blocks(0, 420 , 170 , 1000 , PURPLE)
		draw_blocks(250, 420,170, 1000, PURPLE)
		draw_blocks(400, 360, 120, 1000, PURPLE)
		draw_blocks(600, 360, 100, 500, PURPLE)
		draw_blocks(700, 300, 120, 2000, PURPLE)
		draw_blocks(820, 420, 180, 1000, PURPLE)
		draw_blocks(1100, 300, 200, 10, WHITE)
	elif screen_number == 2:
		draw_blocks(1350, 250, 180, 10, WHITE)
		draw_blocks(1580, 350, 180, 10, WHITE)
		draw_blocks(1780, 420, 250, 100, PURPLE)
		draw_blocks(2080, 380, 40, 30, WHITE)
		draw_blocks(2150, 420, 30, 30, WHITE)
		draw_blocks(2230, 420, 180, 100, PURPLE)
	elif screen_number == 3:
		draw_blocks(2450, 370, 30, 30, WHITE)
		draw_blocks(2500, 340, 30, 30, WHITE)
		draw_blocks(2580, 320, 60, 30, WHITE)
		draw_blocks(2670, 400, 80, 20, WHITE)
		draw_blocks(2790, 450, 350, 100, PURPLE)
	# keys = pygame.key.get_pressed()
	# keys(p)
	# do_jumping(p)
	# pygame.draw.circle(screen, BLUE, (p.x, p.y - p.jump_offset),radius,length)
	# platform_color = PINK
	# if p.jump_offset == 0:
	# 	platform_color = BLUE
	# # Make mario jump 
	# if jump == True:
		# Write the code to make mario jump
		# jump = False
		# pass

	# draw_circle()
	#### Update display
	pygame.display.update()

	time.sleep(0.001)