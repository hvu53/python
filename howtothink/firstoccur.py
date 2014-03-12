def firstoccur(substr, theString):
	index = theString.index(substr)
	if index < 0: #substr doesnt exist in theStr
		return theString
	return_str = theString[:index] + theString[index + len(substr):]
	return return_str

print firstoccur('an', 'banana')