import turtle 
turtle.shape ("turtle")

# def tree(branchLen,t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         tree(branchLen-15,t)
#         t.left(40)
#         tree(branchLen-15,t)
#         t.right(20)
#         t.backward(branchLen)

# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(75,t)
#     myWin.exitonclick()
def main():
	t = turtle.Turtle()
	t.left()
	t.up()
	t.backward()
	t.down
def tree(branchLen,t):
	if branchLen < 5:
		return
		t.forward(100)
		t.right(20)
		tree(45 * 0.6, t)
		t.left(40)
		tree(45-15,t)
		t.right(20)
		t.backward(45)


		# t.forward(50)
		# turtle.forward(25)
		# turtle.left(5)
		# turtle.forward(50)
		# turtle.left(35)
		# turtle.forward(20)
		# turtle.left(180)
		# turtle.forward(25)
		# turtle.left(120)
		# turtle.forward(25)
turtle.exitonclick()