def backward(infile):
	for line in reversed(list(open("infile"))):
		print(line.rstrip())