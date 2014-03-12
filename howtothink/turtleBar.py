import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


xs = [48,117,200,240,160,260,220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0-border,0-border,40*numbars+border,maxheight+border)


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.pensize(3)


for i in xs:
    if i >= 200:
        tess.fillcolor("red")
    elif i>100 and i<200:
        tess.fillcolor("yellow")
    else:
        tess.fillcolor("green")
    drawBar(tess, i)

wn.exitonclick()
