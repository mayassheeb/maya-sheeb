from turtle import Turtle
import random
from turtle import *
import turtle
colormode(255)
class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		register_shape("square", ((0,0),(size, 0), (size,size), (0,size)))
		self.shape("square")

	def random_color(self):
		R = random.randint(0, 255)
		B = random.randint(0, 255)
		G = random.randint(0, 255)
		color = (R,G,B)
		self.color(color)

square = Square(200)

square.random_color()
turtle.exitonclick()