# "[" means we want to save the state of our turtle (its position & heading) so that we can come back to this position later
# "]" tells the turtle to warp to the most recently saved position
# use list: save the heading and position of the turtle as a list [heading x y]

import turtle

def drawLsystem(aTurtle, instructions, angle, distance):
	saveInfoList = []
	for cmd in instructions:
			if cmd == 'F':
				aTurtle.forward(distance)
			elif cmd == 'B':
				aTurtle.backward(distance)
			elif cmd == '+':
				aTurtle.right(angle)
			elif cmd == '-':
				aTurtle.left(angle)
			elif cmd == '[':
				saveInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
				print(saveInfoList)
			elif cmd == ']':
				newInfo = saveInfoList.pop()
				aTurtle.setheading(newInfo[0])
				aTurtle.setposition(newInfo[1], newInfo[2])
				# print(newInfo)
				# print(saveInfoList)
			else:
				print('Error:', cmd, 'is an unknown command')

t = turtle.Turtle()
#inst = "FF[-F[-X]+X]+F[-X]+X"
inst = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF[-FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X"
t.setposition(0,-200)
t.left(90)
drawLsystem(t,inst,30,2)