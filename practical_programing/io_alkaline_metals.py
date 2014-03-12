l = []
with open('io_alkaline_metals.txt', 'r') as f:
	for line in f:
		x = line.strip().split(' ')
		l.append([x[0], x[1:]])
print l