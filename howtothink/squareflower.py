import turtle

wn = turtle.Screen()
wn.bgcolor("pink")

def drawSquare(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)
       
def drawPat(t,numsides,size):
    for i in range(numsides):
        drawSquare(t,size)
        t.penup()
        t.right(360/numsides)
        t.pendown()
        

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

drawPat(tess,20,100)
