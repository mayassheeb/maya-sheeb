import turtle 
turtle.shape("turtle")
sidelenght=100
angle=60
for x in range(4):
	turtle.forward(sidelenght)
	turtle.right(angle)
	turtle.forward(sidelenght)
	turtle.right(angle)
    
turtle.exitonclick()

