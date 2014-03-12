from molecule import Molecule
from atom import Atom

def read_molecule(r):
	""" (reader) -> Molecule
	Read a single molecule from r and return it
	or return None to signal end of file
	"""
	# if there isnt another line, we're at the end of the file
	line = r.readline()
	if not line:
		return None

	# name of the molecule: "COMPND		name"
	key, name = line.split()

	# other lines are either "END" or "ATOM num kind x y z"
	molecule = Molecule(name)
	reading = True

	while reading:
		line = r.readline()
		if line.startswith('END'):
			reading = False
		else:
			key, num, kind, x, y, z = line.split()
			molecule.add(Atom(num, kind, float(x), float(y), float(z)))

	return molecule

