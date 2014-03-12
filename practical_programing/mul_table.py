def mul_table(n):
	for i in range(1, n+1):
		print ('\t', i, end='')
	print()
	for k in range(1,n+1):
		print(k, end='')
		for j in range(1,n+1):
			print ('\t', k*j, end='')
		print()
	return ''
print(mul_table(5))