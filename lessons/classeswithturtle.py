import turtle
from turtle import Turtle

class circle(Turtle):
	def __init__(self,color, size,shape):
		Turtle.__init__(self)
		self.shapesize(size)
		self.color(color)
		self.shape(shape)

class box1(circle):
	def ball(self, pen_color,x,y):
		self.pencolor(pen_color)
		self.up()
		self.goto(x,y)
		self.down()

ball1 = box1("orange", 7, "circle")
ball1.ball("blue",100,100)

square1 = box1("pink", 12, "square")
square1.ball("black", -80,-60)

ball2 = box1("green", 6, "triangle")
ball2.ball("black", -60, 150)

turtle.exitonclick()
