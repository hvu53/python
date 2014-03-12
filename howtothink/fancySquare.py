import turtle

def drawSprite(t,numlegs, leglen):
	angle = 360/numlegs
	for i in range(numlegs):
		t.forward(leglen)
		t.backward(leglen)
		t.left(angle)

def drawFancySquare(t, sz, nleg, leglen):
	for i in range(4):
		t.forward(sz)
		drawSprite(t,nleg, leglen)
		t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
drawFancySquare(tess,100,10,15)

wn.exitonclick()