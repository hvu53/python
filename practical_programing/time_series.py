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