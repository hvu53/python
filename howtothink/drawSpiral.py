import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

def drawSpiral(t, angle):
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length +=2

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

tess.penup()
tess.backward(110)
tess.pendown()

drawSpiral(tess, 90)

tess.penup()
tess.home()

tess.forward(90)
tess.pendown()

drawSpiral(tess, 89)