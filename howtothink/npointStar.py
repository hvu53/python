import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

def drawStar(t, n):
    for i in range(n):
    	t.forward(100)
    	t.left(180 - 180/n)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)


drawStar(tess, 10)