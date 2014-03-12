def find_dup(l):
	""" list -> set
	take a list of integers as input, returns a set of int that occur 2 or more times
	>>>find_dups([1,1,2,3,4,2])
	{1,2}
	"""
	elem_set = set()
	dups_set = set()
	for i in l:	
		original_len = len(elem_set)
		elem_set.add(i)
		after_len = len(elem_set)
		if original_len == after_len:
			dups_set.add(i)

	return dups_set

print(find_dup([1,1,2,3,4,2]))

