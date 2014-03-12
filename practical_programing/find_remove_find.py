#import doctest
def find_two_smallest(L):
	""" (list of float) -> tuple of (int, int)
	Return a tuple of the indices of the two smallest values in list L
	>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
	(6, 7)
	"""
	# find the index of the minimum and remove that item
	smallest = min(L)
	min1 = L.index(smallest)
	L.remove(smallest)
	# find the index of the new minimum
	new_smallest = min(L)
	min2 = L.index(new_smallest)
	# put smallest back into L
	L.insert(min1,smallest)
	# fix min2 in case it was affected by the reinsertion
	if min1 <= min2:
		min2 +=1

	return(min1,min2)

#print doctest.testmod()