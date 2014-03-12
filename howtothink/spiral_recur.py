import turtle

myturtle = turtle.Turtle()
wn = turtle.Screen()

def drawSpiral(myturtle, lineLen):
	if lineLen > 0:
		myturtle.forward(lineLen)
		myturtle.right(90)
		drawSpiral(myturtle, lineLen-5)

drawSpiral(turtle,200)
wn.exitonclick()