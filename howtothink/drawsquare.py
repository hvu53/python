import turtle

wn = turtle.Screen()
wn.bgcolor("pink")

def drawsquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

tess = turtle.Turtle()
tess.color("blue")
tess.fillcolor("green")
tess.pensize(3)

for i in range(5):
    drawsquare(tess,20)
    tess.penup()
    tess.forward(40)
    tess.pendown()
