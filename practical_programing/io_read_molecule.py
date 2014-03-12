def read_molecule(reader):
	""" (file open for reading) -> list or NoneType
	Read a single molecule from reader and return it, or return None to
	signal end of file. The first item in the result is the name of the compound;
	each list contains an atom type & the X,Y, and X coordiantes of that atom
	"""

	# if there isnt another line, we're at the end of the file
	line = reader.readline()
	if not line:
		return None

	# name of the molecule: "COMPND 	name"
	key, name = line.split()

	# other lines are either "END" or "ATOM num atom_type x y z"
	molecule = [name]
	reading = True

	serial_number = 1
	while reading:
		line = reader.readline()
		if line=="" or line=="\t" or line.startswith("CMNT"):
			continue
	# parse all the atoms in the molecule
		if line.startswith('END'):
			reading = False
		else:
			key,num,atom_type,x,y,z = line.split()
			if int(num) != serial_number:
				print('Expected serial number {0} but got {1}'.format(serial_number,num))
			molecule.append([atom_type,x,y,z])
			serial_number += 1

	return molecule

def read_all_molecules(reader):
	""" (file open for reading) -> list
	Read zero or more molecules from reader, returning a list of molecule
	information
	"""
	# the list of molecule information
	result = []
	reading= True
	while reading:
		molecule = read_molecule(reader)
		if molecule: # none is treated as False in if statement
			result.append(molecule)
		else:
			reading = False
	return result

if __name__ == '__main__':
	molecule_file = open('multimol.pdb', 'r')
	molecules = read_all_molecules(molecule_file)
	print(molecules)