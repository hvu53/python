filename = input("Enter file name here: ")
f = filename+'.bak'
with open(f, 'w') as output_file:
	for line in filename:
		output_file.write(line)