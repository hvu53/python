def linear_search(lst, value):
	"""
	return the index of the first occurence of value in lst
	>>> linear_search([2,5,1,-3],5)
	"""
	#add the sentinel
	lst.append(value)
	i= 0

	# keep going until we find value
	while lst[i] != value:
		i += 1

	# remove the sentinel
	lst.pop()

	# if we reached the end of the list we didnt find value
	if i == len(lst):
		return -1
	else:
		return i