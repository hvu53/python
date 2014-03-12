import time
import find_remove_find
import sort_then_find
import walk_through

def time_find_two_smallest(find_func, lst):
	""" (function, list) -> float
	return how many seconds find_func(lst) took
	"""

	t1 = time.perf_counter()
	find_func(lst)
	t2 = time.perf_counter()
	return (t2-t1)*1000

if __name__ == '__main__':
	# gather the sea level pressures
	sea_levels = []
	sea_levels_file = open('sea_levels.txt','r')
	for line in sea_levels_file:
		sea_levels.append(float(line))
	# time each of the approaches
	find_remove_find_time = time_find_two_smallest(find_remove_find.find_two_smallest, sea_levels)
	sort_then_find_time = time_find_two_smallest(sort_then_find.find_two_smallest, sea_levels)
	walk_through_time = time_find_two_smallest(walk_through.find_two_smallest, sea_levels)

	#print(sea_levels)
	print('"Find remove find" took {:.2f}ms.'.format(find_remove_find_time))
	print('"Sort, get minimums" took {:.2f}ms.'.format(sort_then_find_time))
	print('"walk through" took {:.2f}ms.'.format(walk_through_time))