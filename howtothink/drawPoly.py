import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

def drawsquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
alex = turtle.Turtle()
alex.color("pink")
alex.pensize(5)

for i in range(1,6):
    drawsquare(alex,i*20)
    alex.penup()
    alex.forward(-10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()
