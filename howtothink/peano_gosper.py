import turtle

def createLSystem(numIters, axiom):
	startString = axiom
	endString = ""
	for i in range(numIters):
		endString = processString(startString)
		startString = endString

	return endString

def processString(oldStr):
	newstr = ""
	for ch in oldStr:
		newstr = newstr + applyRules(ch)

	return newstr

def applyRules(ch):
	newstr = ""
	if ch == "X":
		newstr = 'X+YF++YF-FX--FXFX-YF+'
	elif ch == "Y":
		newstr = '-FX+YFYF++YF+FX--FX-Y'
	else:
		newstr = ch

	return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
	for cmd in instructions:
		if cmd == 'F':
			aTurtle.forward(distance)
		elif cmd == 'B':
			aTurtle.backward(distance)
		# elif cmd == 'L':
		# 	aTurtle.left(angle*2)
		# elif cmd == 'R':
		# 	aTurtle.right(angle*2)
		elif cmd == '+':
			aTurtle.right(angle)
		elif cmd == '-':
			aTurtle.left(angle)
		else:
			pass

def main():
	inst = createLSystem(5,"FX") # create the string
	print(inst)
	t = turtle.Turtle()
	wn = turtle.Screen()

	t.up()
	t.back(100)
	t.down()
	t.speed(9)
	drawLsystem(t,inst, 60,5)

	wn.exitonclick()

main()