import turtle
import time
import random
from basicgame import Ball1
turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0001
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
MYBALL = Ball1(300,300,10,10,50, "RED")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10 
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5 
MAXIMUM_BALL_DX = 5 + 50
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

Balls= []

for x in range (NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	if dx == 0:
		dx =random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy == 0:
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

	r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	ball2 = Ball1(x,y,dx,dy,r,color)
	Balls.append(ball2)



def move_all_balls():
	for ball in Balls:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

	
def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False

	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()

	ball_a_rad1= ball_a.r
	ball_b_rad2= ball_b.r


	D= ((x2-x1)**2+(y2-y1)**2)**0.5
	if D <= ball_b_rad2 + ball_a_rad1:
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in Balls:
		for ball_b in Balls:
			if collide(ball_a, ball_b) == True:

				ball_a_rad1=ball_a.r
				ball_b_rad2=ball_b.r 
				if ball_a_rad1 > ball_b_rad2:
						new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
						new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
						new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
						if new_dx == 0:
							random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

						new_dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
						if new_dy == 0:
							random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

						new_r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
						new_color = (random.random(), random.random(), random.random())
						ball_a.color(new_color)
						ball_b.color(new_color)
						ball_b.goto(new_x, new_y)
				if ball_b_rad2 > ball_a_rad1:
						new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
						new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
						new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
						if new_dx == 0:
							random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

						new_dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
						if new_dy == 0:
							random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

						new_r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
						new_color = (random.random(), random.random(), random.random())
						ball_a.color(new_color)
						ball_a.goto(new_x, new_y)
	return True


def check_myball_collision():
	for ball in Balls:
		if (collide (ball, MYBALL)) == True:
			MYBALL_r=MYBALL.r
			ball_r =ball.r
			if ball_r>MYBALL_r:
				MYBALL.hideturtle()
			if MYBALL_r > ball_r:
				MYBALL.r = MYBALL.r +4
				MYBALL.shapesize(MYBALL.r/10)
				new_x5 = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				new_y5 = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				new_dx5 = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				if new_dx5 == 0:
					dx5=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				new_dy5= random.randint (MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				if new_dy5==0:
					dy5= random.randint (MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				new_r5=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				new_color5=(random.random(), random.random(), random.random())

				ball.goto(new_x5, new_y5)
				ball.dx= new_dx5
				ball.dy= new_y5
				ball.r=new_r5
				ball.shapesize(new_r5/10)
				ball.color(new_color5)




def movearound():
	MYBALL.ondrag(MYBALL.setpos)


while RUNNING:
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	move_all_balls()
	turtle.getscreen().update()
	# movearound()
	# time.sleep(0.01)
	check_all_balls_collision()
	check_myball_collision()

	if check_myball_collision()== False:
		RUNNING = False
		turtle.write("game over")
	
turtle.getscreen().update()
	time.sleep(0.02)


		# if rad1 > rad2:
		# 	turtle.hideturtle()
		# # if D < 10: 
		# elif ad2> rad1:
		# 	turtle.hideturtle()

mainloop()

