import random
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.shape("turtle")

def isInScreen(w,t):
	leftBound = -(wn.window_width()/2)
	rightBound = wn.window_width()/2
	topBound = wn.window_height()/2
	bottomBound = -(wn.window_height()/2)

	turtleX = tess.xcor()
	turtleY = tess.ycor()

	stillIn = True
	if turtleX > rightBound or turtleX <leftBound:
		stillIn = False
	if turtleY > topBound or turtleY < bottomBound:
		stillIn = False

	return stillIn

while isInScreen(wn,tess):
	coin = random.randrange(0,2)
	if coin ==0:
		tess.left(90)
	else:
		tess.right(90)
	tess.forward(50)

wn.exitonclick()