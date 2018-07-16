import turtle
turtle.shape("turtle")

input=3

if input==4:
	turtle.forward(100)
	turtle.right (90)
elif input==3:
	turtle.fillcolor("pink")
	turtle.begin_fill()
	turtle.circle(89)
	turtle.end_fill()
	turtle.fillcolor("blue")
	turtle.begin_fill()
	for x in range(4):
		turtle.forward(100)
		turtle.right(90)
		turtle.forward(30)
		turtle.left(60)
		turtle.circle(14)
		turtle.end_fill()
		turtle.fillcolor("green")
		turtle.begin_fill()
		turtle.forward(55)
		turtle.right(120)
		turtle.circle(30)
	turtle.end_fill()
	
elif input==2:
	turtle.foward(50)

turtle.exitonclick()