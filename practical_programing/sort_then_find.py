#import doctest
def find_two_smallest(L):
	""" (list of float) -> tuple of (int, int)
	Return a tuple of the indices of the two smallest values in list L
	>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
	(6, 7)
	"""
	# sort a copy of L
	temp_list = sorted(L)
	# get the 2 smallest number
	smallest = temp_list[0]
	next_smallest = temp_list[1]
	# find their indices in the original list L
	min1 = L.index(smallest)
	min2 = L.index(next_smallest)
	# return the two incdices
	return (min1,min2)

#print doctest.testmod()