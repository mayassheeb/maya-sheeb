from turtle import*
import random
import math
import time
import turtle
turtle.window_width()
turtle.window_height()
# screen = Screen()

# wn = turtle.screen()
turtle.bgcolor("black")
turtle.title("Piggy Maze Game")
turtle.setup(700,700)

#create pen
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)

class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.color("blue")
		self.penup()
		self.speed(0)
		self.gold = 0

	def go_up(self):
		#calculate the spot to move to
		move_to_x = player. xcor()
		move_to_y = player. ycor()+ 24
		#check if the space has a wall
		if (move_to_x, move_to_y)not in walls:
			self.goto(move_to_x, move_to_y)

		# self.goto(self.xcor(), self.ycor() + 24)

	def go_down(self):
		#calculate the spot to move to
		move_to_x = player. xcor()
		move_to_y = player. ycor() - 24
		#check if the space has a wall
		if (move_to_x, move_to_y)not in walls:
			self.goto(move_to_x, move_to_y)

		# self.goto(self.xcor(), self.ycor() - 24)


	def go_left(self):
		#calculate the spot to move to
		move_to_x = player. xcor() -24
		move_to_y = player. ycor() 
		#check if the space has a wall
		if (move_to_x, move_to_y)not in walls:
			self.goto(move_to_x, move_to_y)
		# self.goto(self.xcor() -24, self.ycor())

	def go_right(self):
		#calculate the spot to move to
		move_to_x = player. xcor() +24
		move_to_y = player. ycor() 
		#check if the space has a wall
		if (move_to_x, move_to_y)not in walls:
			self.goto(move_to_x, move_to_y)

	# def is_collision(self, other):
	# 	a = self.xcor()-other.xcor()
	# 	b = self.ycor()-other.ycor()
	# 	distance = math.sqrt((a ** 2)+ (b ** 2))

	# 	if distance < 5:
	# 		return True
	# 	else:
	# 		return False

class Treasure (turtle.Turtle):
	def __init__(self, x,y):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.color("gold")
		self.penup()
		self.speed(0)
		self.gold = 100
		self.goto(x,y)

	def destroy(self):
		self.goto(2000, 2000)
		self.hideturtle()


		
	

#create rows list 
rows = [""]

#define first row
row_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXX  B XX  XXXXXXX",
"X                XXXXXXXX",
"X              XXXXXXXXXX",
"XXX   XXXX     XXXXXXXXXX",
"XXXX   XXXXX   XXXXXXXXXX",
"XXXXX  XXXXXX    XXXXXXXX",
"XXXXXX     XXX     XXXXXX",
"XXXXXXXXX       XXXXXXXXX",
"XXXXX      XX  XXXXXX  XX",
"XXX     XX XX    XXXXXXXX",
"XX  XXXX  XXXXXX   XXXXXX",
"X  XXXXXXX   XX  XXXXXXXX",
"X  XXXXXXX       XXXXXXXX",
"X              XXXXXXXXXX",
"XXX   XXXX     XXXXXXXXXX",
"XXXX   XXXXX   XXXXXXXXXX",
"XXXXX  XXXXXX    XXXXXXXX",
"XXXXXX     XXX     XXXXXX",
"XXXXXXXXX       XXXXXXXXX",
"XXXXX      XX  XXXXXXXXXX",
"XXXXXXXXX  XX    XXXXXXXX",
"XXXXXXXX  XXXXXX   XXXXXX",
"XXXXXXXX   XXXXXX  XXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Add a treasures list
treasure = []
#add maze to mazes list
rows.append(row_1)

#create level Setup Function
def setup_maze(row):
	for y in range(len(row)):
		for x in range (len(row[y])):
			#get the charecter at each x, y cordinate
			#note the order of y and x in the next line
			charecter = row[y][x]
			#calculate the screen x,y coordinates 
			screen_x = -288 + (x * 24)
			screen_y = 288 - (y * 24)

			#Check if it is an X (representing a wall)
			if charecter == "X":
				pen.goto(screen_x, screen_y)
				pen.stamp()
				#add cordinates to wall list
				walls.append((screen_x, screen_y))

			#check if it is a P(representing the player)
			if charecter == "P":
				player.goto(screen_x, screen_y)

			#Check if it is a T (representing Treasure)
			# if charecter == "T":
			# 	treasures.append(Treasure(screen_x, sceen_y))

#creat class instances
pen = Pen()
player = Player()

#create wall cordinate list
walls = []

#setp the rows
setup_maze(rows[1])
print (walls)

#keyboard 
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

#Turn off screen updates
turtle.tracer(0)


#main Game Loop
while True:
	#check for player collision with treasre 
	#iterate through treasure list 
	# for treasure in treasures:
	# 	if player.is_collision(treasure):
			#Add the treasure gold to the player golder
			# player.gold += treasure.gold
			# print ("Player Gold: {}". format(player.gold))
			#Destroy the treasure
			# treasure.destroy()
			#Remov the treasure from the treasures list
			# treasures.remove(treasures)
	#update scren
	turtle.update()

exitonclick()
 