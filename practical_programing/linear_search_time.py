import time
import linear_search_1
import linear_search_2
import linear_search_3
import binary_search

def time_it(search, L, v):
	""" (function, object, list) -> number
	Time how long it takes to run function search to find
	value v in list L
	"""
	t1 = time.perf_counter()
	search(L,v)
	t2 = time.perf_counter()
	return (t2-t1)*1000.0

def print_times(v, L):
	""" (object, list) -> NoneType
	print the number of milliseconds it takes for linear_search(v, L)
	to run for list.index
	"""
	# get list.index's running time
	t1 = time.perf_counter()
	L.index(v)
	t2 = time.perf_counter()
	index_time = (t2-t1) * 1000.0

	# get the other three running times
	while_time = time_it(linear_search_1.linear_search, L, v)
	for_time = time_it(linear_search_2.linear_search, L, v)
	sentinel_time = time_it(linear_search_3.linear_search, L, v)
	binary_time = time_it(binary_search.binary_search, L, v)
	print("{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}\t{5:.2f}".format(v, while_time, for_time, sentinel_time, index_time, binary_time))

L = list(range(10000001))

print_times(10,L)
print_times(500000, L)
print_times(1000000,L)