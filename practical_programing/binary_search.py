import doctest
def binary_search(L,v):
	""" (list,obhighect) -> int
	return the index of the first occurence of value in lst
	>>> binary_search([1,3,4,4,5,7,9,10],1)
	0
	>>> binary_search([2,5,1,-3],5)
	1
	>>> binary_search([1,3,4,4,5,7,9,10],4)
	2
	>>> binary_search([1,3,4,4,5,7,9,10],5)
	4
	"""
	# mark the left & right incides of the unknow section
	low = 0
	high = len(L) -1
	while low != high+1:
		m = (low+high)//2
		if L[m] < v:
			low = m+1
		else:
			high = m -1

	if 0 <= low < len(L) and L[low] ==v:
		return low
	else:
		return -1

# if __name__ == "__main__":
# 	import doctest
# 	print doctest.testmod()