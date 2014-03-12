def sum_number_pairs(infile,outfile):
	""" (file open for reading, str) -> NoneType

	Read the data from infile, which contains 2 floats per line separated by
	a space. Open file named outfile and, for each line in infile, write a line
	to the outfile that contains the 2 floats from the corresponding line of
	infile plus a spce & the sum of the 2 floats

	"""
	with open(outfile, 'w') as f:
		for num_pair in infile:
			num_pair = num_pair.strip()
			operands = num_pair.split()
			total = float(operands[0]) + float(operands[1])
			newline = '{0} {1}\n'.format(num_pair,total)
			f.write(newline)

sum_number_pairs(open('num_pairs.txt','r'),'num_pair_out.txt')