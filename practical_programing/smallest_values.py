import time_series

def smallest_value(reader):
	""" (file open for reading) -> NoneType
	Read and process reader and return the smallest value after
	the time_series header
	"""

	line = time_series.skip_header(reader).strip()

	# now line contains the first data value; this is also the smallest value
	# found so far
	if line == '':
			smallest =0
			line = 0

	smallest = int(line)

	for line in reader:
		line = line.strip()
		if line == "-":
			continue
		value = int(line)
		smallest = min(smallest,value)

	return smallest

if __name__ == '__main__':
	with open('hopedale.txt','r') as infile:
		print(smallest_value(infile))