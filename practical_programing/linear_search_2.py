def linear_search(lst, value):
	"""
	return the index of the first occurence of value in lst
	>>> linear_search([2,5,1,-3],5)
	"""
	for i in range(len(lst)):
		if lst[i] == value:
			return i
	return -1