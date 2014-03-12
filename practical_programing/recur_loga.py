def myLog(x,b):
	# if x ==1:
	# 	return 0
	# return myLog(x-1,b)
	count = 0
	while x >1:
		x /= b
		count+=1
	return count
print myLog(16,2)
print myLog(15,3)