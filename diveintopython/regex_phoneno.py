phonePattern = re.compile(r'''
							# dont match beginning of string, number can start anywhere
		(\d{3})		# area code is 3 digit
		\D*				# optional separator is any number of non-digits
		(\d{3})		# trunk is 3 digits
		\D*				# optional separator
		(\d{4})		# rest of number is 4 digits
		\D*				# optional separator
		(\d*)			# extension is optional and can be any number of digits
		$					# end of string
	''')


print phonePattern.search('work 1-(800) 555.1212 #1234').groups()
print phonePattern.search('800-555-1212').groups()