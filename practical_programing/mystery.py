import doctest
def mystery_function(values):
	"""
	[list,list] -> [list,list]
	reverse sublist in list
	>>> mystery_function([[1,2,3,4,5],[6,7,8,9,0]])
	[[5, 4, 3, 2, 1], [0, 9, 8, 7, 6]]
	"""
	result = []
	for sublist in values:
		result.append([sublist[0]])
		for i in sublist[1:]:
				result[-1].insert(0,i)
	return result

print mystery_function([[1,2,3,4,5],[6,7,8,9,0]])
print doctest.testmod()