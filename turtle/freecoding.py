import turtle
turtle.shape("turtle")
turtle.speed(12) 
def draw_circle(color,radius):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(radius)
	turtle.end_fill()
turtle.right(90)
draw_circle("black",150)
turtle.penup()
turtle.left(90)
turtle.forward(160)
turtle.left(90)
turtle.forward(10)
turtle.forward(30)
turtle.pendown()
turtle.right(5)
draw_circle("white",57)
turtle.penup()
turtle.right(90)
turtle.forward(12)
turtle.right(90)
turtle.forward(3)
turtle.pendown()
draw_circle("white",39)
turtle.penup()
turtle.left(30)
turtle.forward(15)
turtle.pendown()
draw_circle("black",20)
turtle.penup()
turtle.right(155)
turtle.forward(50)
turtle.pendown()
draw_circle("black",30)
turtle.end_fill()
turtle.penup()
turtle.right(50)
turtle.backward(10)
turtle.pendown()
turtle.right(180)
turtle.forward(60)
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.left(90)
turtle.forward(5)
turtle.right(196)
turtle.exitonclick()