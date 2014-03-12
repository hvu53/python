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

def find_largest(line):
	""" (str) -> int
	return the largest value in line, which is a whitespace-delimited string
	of integers that each end with a '.'
	>>> find_largest('1. 3. 2. 5. 2.')
	"""
	# the largest value seen so far
	largest = -1
	for value in line.split():
		# remove the trailing period
		v = int(value[:-1])
		# if we find a larger value, remember it
		if v > largest:
			largest = v

	return largest

def process_file(reader):
	""" (file open for reading) -> int
	Read and process reader, which must start with a time_series header.
	Return the largest value after the header. There may be multiple pieces
	of data on each line
	"""

	# find and print the first piece of data
	line = skip_header(reader).strip()
	
	# the largest value so far is the largest on this first line of data
	largest = find_largest(line)

	# check the rest of the lines for larger values
	for line in reader:
		large = find_largest(line)
		if large > largest:
			largest = large
	return largest

if __name__ == '__main__':
	with open('lynx.txt','r') as f:
		print(process_file(f))