infile = open("studentdata.txt", "r")

aline = infile.readline()
while aline:
	items = aline.split()
	total = 0
	for i in items[1:]:
		total += int(i)
	print (items[0], total)
	# if len(items[1:]) > 6:
	# 	print(items[0])
	aline = infile.readline()
infile.close()