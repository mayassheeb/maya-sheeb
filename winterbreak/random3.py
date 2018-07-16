from turtle import*
import random


class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.radius=radius
		self.shapesize(radius/10)
		self.color(color)
		self.speed(speed)

	def check_collision(ball1, ball2):
		(x1,y1) = ball1 
		(x2,y2) = ball2
		ball1.radius= rad1
		ball2.radius= rad2
		D= ((x2-x1)**2+(y2-y1)**2)**0.5
		if D =< rad1+rad2: 
			print collision