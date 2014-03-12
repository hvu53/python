def sum_of_squares(xs):
	newlist = [item**2 for item in xs]
	sum = 0
	for i in newlist:
		sum +=i
	return sum

print sum_of_squares([2, 3, 4])