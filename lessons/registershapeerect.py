from turtle import Turtle
import random
from turtle import *
import turtle
colormode(255)
class Rectangle(Turtle):
	def __init__(self, length, width):
		Turtle.__init__(self)
		register_shape("rectangle", ((0,0),(length, 0), (length,width), (0,width)))
		self.shape("rectangle")

	def random_color(self):
		R = random.randint(0, 255)
		B = random.randint(0, 255)
		G = random.randint(0, 255)
		color = (R,G,B)
		self.color(color)

rectangle = Rectangle(50, 200)


rectangle.random_color()
turtle.exitonclick()