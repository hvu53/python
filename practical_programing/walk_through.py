#import doctest
def find_two_smallest(L):
	""" (list of float) -> tuple of (int, int)
	Return a tuple of the indices of the two smallest values in list L
	>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
	(6, 7)
	"""
	# set min1 and min2 to the indices of the smallest and next smallest values at the beginning of L
	if L[0] < L[1]:
		min1, min2 = 0,1
	else:
		min1, min2 = 1,0
	# Examine each value in the list in order
	for i in range(2,len(L)):
		# Update these values when a new smaller value is found
		if L[i] < L[min1]:
			min2 = min1
			min1 = i
		elif L[i] <L[min2]:
			min2 = i
	# return the two indices
	return (min1,min2)

#print doctest.testmod()