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
	if ch == "L":
		newstr = '+RF-LFL-FR+'
	elif ch == "R":
		newstr = '-LF+RFR+FL-'
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
			print('Error:', cmd, 'is an unknown command')

def main():
	inst = createLSystem(4,"L") # create the string
	print(inst)
	t = turtle.Turtle()
	wn = turtle.Screen()

	t.up()
	t.back(200)
	t.down()
	t.speed(9)
	drawLsystem(t,inst, 90,20)

	wn.exitonclick()

main()