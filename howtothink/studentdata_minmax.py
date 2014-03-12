infile = open("studentdata.txt", "r")

aline = infile.readline()
while aline:
	items = aline.split()
	print(items[0], "max is", max(items[1:]), "min is", min(items[1:]))
	aline = infile.readline()
infile.close()