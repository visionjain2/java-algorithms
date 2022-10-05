import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor("black")

# Ball variables
ball_size = 10.0
ball_speed = 5
 
# Boundary variables
box_size = 400.0
boundary = (box_size / 2.0) - ball_size

# Paddle variables
paddle_speed = 30
paddle_width = box_size / 6.0
paddle_thickness = paddle_width / 10.0

# For turtle mode
funny = False

#Drawing the box
box_drawer = turtle.Turtle()
box_drawer.penup()
box_drawer.speed(0)
box_drawer.goto(-box_size / 2.0, -box_size / 2.0)
box_drawer.pendown()
box_drawer.color("red")
for i in range(4):
	box_drawer.forward(box_size)
	box_drawer.left(90)
box_drawer.ht()

################################################################
############################ Paddle ############################
################################################################

#Making the paddle
paddle = turtle.Turtle()
paddle.color("aquamarine")
paddle.shape("square")
paddle.shapesize(paddle_thickness/20.0, paddle_width / 20.0)

'''
TODO: Paddle starting position

Move the paddle so that it starts at the coordinates (0, -boundary + 20)
'''
paddle.penup()
paddle.speed(0)
paddle.goto(0,-boundary + 20)

'''
TODO: Move paddle with arrow keys

1) If the user presses the right arrow key, the paddle moves to the right
by paddle_speed but only if the right edge of the paddle is less than boundary.

2) If the user presses the left arrow key, the paddle moves to the left
by paddle_speed but only if the left edge of the paddle is within the boundary.

Hint: paddle.xcor() will give you the x coordinate of the middle of the paddle.
How can you use this value and paddle_width to get the x coordinates of the 
left and right edges of the paddle?
'''

#Paddle goes right when key pressed, only if within boundaries
def paddle_right():
	if (paddle.xcor() + paddle_width / 2.0) < boundary:
		paddle.forward(paddle_speed)

#Paddle goes left when key pressed, only if within boundaries
def paddle_left():
	if (paddle.xcor() - paddle_width / 2.0) > -boundary:
		paddle.backward(paddle_speed)

screen.onkey(paddle_right, "Right")
screen.onkey(paddle_left, "Left")

################################################################
############################ Bricks ############################
################################################################

# Brick variables
num_bricks = 10
gap_size = 10.0
brick_width = (box_size - (num_bricks + 1)*gap_size) / num_bricks
brick_thickness = brick_width / 2.0

'''
TODO: Write make_brick_row function

Write the function called make_brick_row that takes in a color and y coordinate.
This function will create one row of bricks, save each brick in a list and
return the list of bricks.

  - Use num_bricks for the number of bricks per row.
  - The color is a string that will tell you the color that you should make that 
	row of bricks.
  - The y coordinate will be the y coordinate of all the bricks in this row.
  - When you make your turtle bricks, you can change the speed of 
  	the brick turtle to 0 so that the bricks are drawn more quickly.
  - Use shape to make each brick a square and use shapesize to change 
  	the size of each brick to (brick_thickness/20.0, brick_width/20.0)

Hint: The x coordinate of the first brick should be 
-box_size/2.0 + gap_size + brick_width/2.0. 
From there, the x coordinate of the second brick will be the 
x coordinate of the previous brick plus brick_width plus gap_size
'''
def make_brick_row(color, y):
	row = []
	xBrick = (- box_size / 2.0) + gap_size + (brick_width / 2.0)
	for i in range(num_bricks):
		brick = turtle.Turtle()
		brick.speed(0)
		brick.shape("square")
		brick.shapesize(brick_thickness / 20.0, brick_width/20.0)
		brick.color(color)
		brick.penup()
		brick.goto(xBrick,y)
		row.append(brick)
		xBrick = xBrick + brick_width + gap_size
	return row


'''
TODO: Create 4 rows of bricks

Call make_brick_row 4 times to create 4 rows and store the list of bricks
that is returned in the variables below (row1, row2, row3, row4).
You can make each brick row whatever color you want.

Hint 1: You'll need to calculate the y coordinate of each row of bricks.
Just like in the previous problem, use the variable box_size to 
calculate the edge of the box.

Hint 2: The y coordinate of the top row of bricks should be the 
y coordinate of the top of the box minus gap_size minus brick_thickness/2.0.
From there, the y coordinate of the next row down will be the y coordinate
of row above minus brick_thickness minus gap_size
'''
y_brick = (box_size / 2.0) - gap_size - (brick_thickness / 2.0)
row1 = make_brick_row("red", y_brick)
row2 = make_brick_row("green", y_brick - ((brick_thickness) + gap_size))
row3 = make_brick_row("blue", y_brick - 2*((brick_thickness) + gap_size))
row4 = make_brick_row("yellow", y_brick - 3*((brick_thickness) + gap_size))

################################################################
############################ Ball ##############################
################################################################

#Making the ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("hot pink")
ball.shape("circle")
ball.penup()
ball.goto(0, paddle.ycor() + (paddle_thickness / 2.0) + ball_size)

# Set the angle of the ball
heading = random.randint(10,170)
print(heading)
ball.setheading(heading)

'''
TODO: Bounce wall

Create a function called bounce_wall that bounces the ball whenever it hits
the boundary.
	- If the ball is at a corner (in other words, its x coordinate 
		and y coordinate are both past the boundaries) then the ball 
		should bounce back in exactly the opposite direction it came from.

One way to do this is to change the angle of the ball if it is past 
the boundary. If you use this approach, use the function heading to get the 
current angle of the ball and the function setheading to change 
the angle of the ball.
	- If the ball is past the left or right boundary, change the angle to be 
		180 minus the current angle
	- If the ball is past the top of the boundary, change the angle to be 
		360 minus the current angle

Example use of heading and setheading:
	turtle_angle = name_of_turtle.heading()

	name_of_turtle.setheading(new_angle)
'''

#Checks for wall collision and changes direction
def bounce_wall():
	if ball.xcor() > boundary or ball.xcor() < -boundary:
		#For corners just turn around
		if ball.ycor() > boundary:
			ball.left(180)
		#For side walls switch angle (always the same geometry)
		else:
			ball.setheading(180 - ball.heading())
	#For top/bottom walls switch angle (always the same geometry)
	elif ball.ycor() > boundary:
		ball.setheading(360 - ball.heading())

'''
TODO: Bounce paddle

Create a function called bounce_paddle that bounces the ball off the paddle.

To check if the ball is touching the paddle,
you have to check that all the following are true:

	1) the ball is heading downwards
	2) the y coordinate of the ball minus the ball size is less 
		than the y coordinate of the top edge of the paddle
	3) the x coordinate of the ball plus the ball size is greater 
		than the x coordinate of the left edge of the paddle
	4) the x coordinate of the ball minus the ball size is less than the x coordinate of right edge of the paddle

If all the above conditions are True, then change the angle of the ball 
to 360 minus the current angle.

Hint: Think about how to use paddle_width to calculate the edges of the paddle
'''

#Checks for paddle collision and changes direction
def bounce_paddle():
	if ball.ycor() - ball_size < paddle.ycor() + (paddle_thickness / 2.0) and 180 < ball.heading():
		if ball.xcor() + ball_size > paddle.xcor() - (paddle_width / 2.0):
			if ball.xcor() - ball_size < paddle.xcor() + (paddle_width / 2.0):
				ball.setheading(360 - ball.heading())

'''
TODO: Bounce brick row

Create a function called bounce_brick_row that accepts a 
list of bricks as an argument.

This function should check whether the ball is touching each brick in the list.
If the ball is touching the brick and the brick is visible, then make sure 
to hide the brick and bounce the ball (just like in bounce_paddle).

To check if a brick is visible, use the isvisible() function on each brick. 
The isvisible function returns True if the brick is still visible.
To hide a turtle you can use the function ht.
	
	Examples:
		name_of_turtle.ht() #hide
		name_of_turtle.isvisible() 

Hint: To check if the ball is touching each brick, think about how you did 
this for the paddle. Remember that in the case of bricks, you'll have to check
whether the ball is within all 4 edges of the brick and it doesn't matter 
in what direction the ball is moving.
'''
def bounce_brick_row(row):
		for brick in row:
			if ball.ycor() + ball_size > brick.ycor() - (brick_thickness / 2.0): # ball up , brick down
				if ball.ycor() - ball_size < brick.ycor() + (brick_thickness / 2.0): # ball down , brick up
					if ball.xcor() + ball_size > brick.xcor() - (brick_width / 2.0):  # ball right , brick left
						if ball.xcor() - ball_size < brick.xcor() + (brick_width / 2.0):  # ball left  , brick right
							if brick.isvisible():
								brick.ht() # hide
								ball.setheading(360 - ball.heading())
							break

def bounce_bricks():
	bounce_brick_row(row1)
	bounce_brick_row(row2)
	bounce_brick_row(row3)
	bounce_brick_row(row4)

################################################################
####################### Turtle mode ############################
################################################################

def turtleMode():
	for brick in row1:
		brick.shape("square")
	for brick in row2:
		brick.shape("circle")
	for brick in row3:
		brick.shape("turtle")
	for brick in row4:
		brick.shape("turtle")
	# paddle.shape("turtle")
	# ball.shape("turtle")
	global funny
	funny = True

screen.onkey(turtleMode, "t")

#######################################################################
################ Gameplay ###############################
################################################################

'''
TODO: Write bricks_gone_row function

Create a function called bricks_gone_row that accepts a list of bricks
as an argument and returns True if all the bricks in that list are not visible.
The function returns False if there is still at least one brick that is visible.

To check if a brick is visible, use the isvisible() function on each brick.
The isvisible function returns True if the brick is still visible.
'''
def bricks_gone_row(row):
	for brick in row:
		if brick.isvisible():
			return False
	return True

'''
TODO: Write bricks_gone function

Create a function called bricks_gone that calls brick_gone_row 4 times:
once on each row (row1, row2, row3, row4).
If all 4 brick rows are gone, then return True. Otherwise return False.
'''
def bricks_gone():
	if bricks_gone_row(row1) and bricks_gone_row(row2) and bricks_gone_row(row3) and bricks_gone_row(row4): # t and t and t and t
		return True
	return False

def startGame():
	lose = False

	# For turtle mode
	counter = 0

	#Make the ball move continuously
	while True:
		ball.forward(ball_speed)
		'''
		TODO: Player loses

		If the ball is below the bottom boundary, then hide the ball turtle,
		set the lose variable to True and break from this while loop.
		'''
		if ball.ycor() < -boundary:
			ball.ht()
			lose = True
			break

		bounce_wall()
		bounce_paddle()
		bounce_bricks()
		'''
		TODO: Call bricks_gone function

		Call the bricks_gone function and if it returns True then break from
		this while loop
		'''
		if bricks_gone():
			break

		##### For turtle mode #####
		# Funny animation that runs when turtle mode is turned on
		counter+=1
		if funny and counter > 300:
			paddle.shapesize(paddle_width/20.0,paddle_width/20.0)
			for i in range(6):
				for brick in row1:
					brick.speed(0)
					brick.left(30)
			for i in range(6):
				for brick in row2:
					brick.speed(0)
					brick.left(30)
			for i in range(6):
				for brick in row3:
					brick.speed(0)
					brick.left(30)
			for i in range(6):
				for brick in row4:
					brick.speed(0)
					brick.left(30)
			counter = 0
		##########################
	
	'''
	TODO: Create writer turtle for game over
	
	Create a turtle that writes either "You lose!" or "You win!"
	depending on the value of the variable lose.

	You can use the function write for the turtle to write text.
	Example:
		name_of_turtle.write("Text to write on screen")

	You'll want to change the color of the turtle to something other than black
	so that you can see the text.

	If you'd like, you can use the function ht to hide the turtle.
	'''
	writer_turtle = turtle.Turtle()
	writer_turtle.color("white")
	writer_turtle.ht()
	if lose: # lose =true
		writer_turtle.write("YOU LOSE!", font=("Arial", 16, "normal"))
	else: # lose = false
		writer_turtle.write("YOU WIN!", font=("Arial", 16, "normal"))

screen.onkey(startGame, "space")
screen.listen()

# Closes the game window when you click the screen
screen.exitonclick()