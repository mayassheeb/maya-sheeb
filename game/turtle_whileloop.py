import turtle
turtle.shape("turtle")
turtle.speed(10)
while True:
	for x in range(4):
		turtle.fd(100)
		turtle.right(90)
	turtle.penup()
	turtle.fd(50)
	turtle.pendown()
	turtle.clear()
	for x in range(4):
		turtle.backward(100)
		turtle.left(90)
	turtle.clear()
	
turtle.exitonclick()