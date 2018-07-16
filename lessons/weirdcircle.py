import turtle 
turtle.shape ("turtle")
turtle.speed(20)

turtle.circle(150)

turtle.penup()
turtle.goto(0,75)
turtle.pendown()
turtle.getscreen()


turtle.circle(75)

turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.getscreen()

for i in range(11):

	turtle.forward(150)
	turtle.left(160)
	turtle.forward(85)

	# turtle.penup()
	# turtle.goto(0,150)
	# turtle.pendown()

	# turtle.left(20)
	# turtle.forward(150)

	# turtle.left(155)
	# turtle.forward(95)

	turtle.penup()
	turtle.goto(0,150)
	# turtle.left(20)
	turtle.pendown()

	turtle.left(36)

# for i in range(10):
#  	turtle.forward(150)
# 	turtle.right(160)
# 	turtle.forward(85)

# 	# turtle.penup()
# 	# turtle.goto(0,150)
# 	# turtle.pendown()

# 	# turtle.left(20)
# 	# turtle.forward(150)

# 	# turtle.left(155)
# 	# turtle.forward(95)

# 	turtle.penup()
# 	turtle.goto(0,150)
# 	turtle.left(20)
# 	turtle.pendown()

# 	turtle.right(36)



# turtle.penup()
# turtle.left(95)
# turtle.forward(50)
# turtle.right(20)
# turtle.pendown()
 
# for i in range(1):
# 	turtle.left(180)
# 	turtle.forward(100)
# 	turtle.backward(200)
# 	turtle.right(25)
# 	turtle.forward(50)

	# turtle.forward(25)
	# turtle.right(90)

	# turtle.left(30)

	# turtle.forward(25)
	# turtle.left(90)

	# turtle.left(40)

	# turtle.forward(25)
	# turtle.left(90)

turtle.exitonclick()