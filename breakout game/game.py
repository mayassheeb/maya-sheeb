"""
Breakout game. Implemented using pygame. 

Bouncing and movement functions taken from this particle simulation: http://www.petercollingridge.co.uk/book/export/html/6.
"""

print("hello world")

import pygame
import math
import breakout
import constants
colors = [constants.PINK, constants.PURPLE, constants.ROSE]

""" 
Paddle: Methods
"""
# Update the position of the paddle. It is confined to the boundaries
# of the screen
def paddle_update_position(paddle):
    location = breakout.get_mouse_location()
    x_position = location[0]
    if x_position >= (constants.SCREEN_WIDTH - constants.PADDLE_WIDTH):
        x_position = constants.SCREEN_WIDTH - constants.PADDLE_WIDTH
    breakout.set_x(paddle, x_position) 


"""
Ball: Methods
"""

# This function must update the coordinates of the ball and changes the 
# direction of the ball bounces of either the left, top, or right walls 
def ball_update_position(ball):
    x = breakout.get_x(ball)
    y = breakout.get_y(ball)
    x_velocity = breakout.get_x_velocity(ball)
    y_velocity = breakout.get_y_velocity(ball)
    new_x = x + x_velocity
    new_y = y + y_velocity
    breakout.set_x(ball, new_x)
    breakout.set_y(ball, new_y)

    if new_x >= constants.SCREEN_WIDTH - constants.BALL_RADIUS:
        breakout.set_x_velocity(ball, x_velocity*-1)
    elif new_x <= constants.BALL_RADIUS:
        breakout.set_x_velocity(ball, x_velocity*-1)

    if new_y <= constants.BALL_RADIUS:
        breakout.set_y_velocity(ball, y_velocity*-1)


# This function must change the direction of the ball when it hits an 
# object 
def ball_bounce_off(ball):
    y = breakout.get_y_velocity(ball)
    breakout.set_y_velocity(ball, y*-1)


"""
Screen Update: Methods
"""
# This function must render all objects on screen using breakout.py draw 
# methods. No objects should be created in this method. 
def draw_objects():
    breakout.clear_screen()
    for i in range (len(bricks)):
        brick= bricks[i]
        x= breakout.get_x(brick)
        y= breakout.get_y(brick)
        w= breakout.get_width(brick)
        h= breakout.get_height(brick)
        c= breakout.get_color(brick)
        breakout.draw_rectangle(x,y,w,h,c)

    # Draw the paddle, ball, and wall of bricks
    x= breakout.get_x(paddle)
    y= breakout.get_y(paddle)
    w= breakout.get_width(paddle)
    h= breakout.get_height(paddle)
    c= breakout.get_color(paddle)
    breakout.draw_rectangle(x, y, w, h, c)

    x = breakout.get_x(ball)
    y = breakout.get_y(ball)
    radius = breakout.get_radius(ball)
    color = breakout.get_color(ball)
    breakout.draw_circle(x,y,radius, color)

    # Tell pygame to actually redraw everything (DON'T CHANGE)
    pygame.display.flip()


# This function must create the set of bricks to be drawn at the top of 
# the screen. 
# This function returns a list of bricks created. 
def build_bricks():
    bricks = []
    for j in range(constants.NUM_ROWS):
        if j == 0:
            color = colors[0]
        elif j == 2:
            color = colors[1]
        elif j == 4:
            color = colors[2]
        for i in range( constants.BRICKS_PER_ROW ):
            x=(i+1)*constants.GAP + i*constants.BRICK_WIDTH
            y=(constants.GAP + constants.BRICK_HEIGHT)*j
            brick = breakout.create_new_brick()
            breakout.set_x(brick, x)
            breakout.set_y(brick, y)
            breakout.set_color(brick, color)
            bricks.append(brick)
    return bricks




# Creating the screen 
breakout.build_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

# Create the ball, paddle, and bricks here using breakout.py functions.
ball=breakout.create_new_ball()
bricks=build_bricks()
paddle = breakout.create_new_paddle()
# These are variables used to detect the state of the game. 
running = True
start = False

while running:

    # Setup the mouse events 
    # DO NOT change this code
    for event in pygame.event.get():
        # If you click the mouse, the ball will start moving 
        if pygame.mouse.get_pressed() == (1, 0, 0):
            start = True 
        if event.type == pygame.QUIT:
            running = False


    if start == True:
        # Make the ball update its position. 
        ball_update_position(ball)


    # Update the position of the paddle based on the mouse
    paddle_update_position(paddle) 
        
    # Check for collisions using breakout.ball_did_collide_with(ball, obj, width, height) 
    if breakout.ball_did_collide_with(ball, paddle, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT):
        ball_bounce_off(ball)

    
    # If ball hits the bottom wall, we lose.
    if breakout.get_y(ball) >= (constants.SCREEN_HEIGHT - constants.BALL_RADIUS):
        running = False

    # If bricks are all broken, you won! 
    if (len(bricks) == 0):
        running = False

    # Else, loop through the entire bricks list to see if the ball collided with any brick 
    for x in range(len(bricks)-1, -1, -1):
        brick = bricks[x]
        if breakout.ball_did_collide_with(ball, brick, constants.BRICK_WIDTH, constants.BRICK_HEIGHT):
            bricks.remove(brick)
            ball_bounce_off(ball)


    # Redraw everything at the end of the while loop
    draw_objects()

pygame.display.update()
