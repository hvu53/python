def skip_header(reader):
	""" (file open for reading) -> str
	skip the header in reader and return the first real piece of data
	"""
	# read the description line
	line = reader.readline()

	# find the first non-comment line
	line = reader.readline()
	while line.startswith('#'):
		line = reader.readline()

	# now line contains the first real piece of data
	return line

def process_file(reader):
	""" (file open for reading) -> NoneType
	Read and print the data from reader, which must start with a single
	description line, then a sequence of lines beginning with '#',
	then a sequence of data
	"""

	# find and print the first piece of data
	line = skip_header(reader).strip()
	print(line)

	# read the rest of the data
	for line in reader:
		line = line.strip()
		print(line)

if __name__ == '__main__':
	with open('hopedale.txt', 'r') as infile:
		process_file(infile)