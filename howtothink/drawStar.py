import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

def drawStar(t,sz):
    for i in range(5):
        t.forward(sz)
        t.left(216)
        
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(2)

drawStar(alex, 130)
