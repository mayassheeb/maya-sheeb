from turtle import Turtle
import random
from turtle import *
import turtle
colormode(255)
class Hexagon(Turtle):
	def __init__(self, n,shape):
		Turtle.__init__(self)
		self.penup()
		sides = random.randint (3,16)
		self.n = n
		self.begin_poly()
		4888830143#######///////..........................................................................................................................................................................................................................................................................................................................................................................................................for x in range(sides):
			self.fd(n)
			self.right(360/sides)
		self.end_poly()
		p = self.get_poly()
		register_shape(shape, p)
		self.shape(shape)
		self.pendown()

	def random_color(self):
		R = random.randint(0, 255)
		B = random.randint(0, 255)
		G = random.randint(0, 255)
		color = (R,G,B)
		self.color(color)

	turtle.setheading(90)
	turtle.heading()
	90.0
	# turtle.heading()
	# 700
	# turtle.left(180)
	# turtle.heading()
	# 100.0
hexagon = Hexagon(70, "k")

hexagon.random_color()
turtle.exitonclick()