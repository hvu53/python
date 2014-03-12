# qbfile = open("qbdata.txt", "r")

# for aline in qbfile:
# 	values = aline.split()
# 	print ('QB', values[0], values[1], 'had a rating of ', values[10])

# qbfile.close()

infile = open("qbdata.txt", "r")

line = infile.readline() # priming read
while line:
	values = line.split()
	print('QB', values[0], values[1], 'had a rating of', values[10])
	line = infile.readline()

#readline will return '' if there s no more line in the file
infile.close()