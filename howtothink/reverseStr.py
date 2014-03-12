def reverseStr(s):
	if s == "":
		return s
	else:
		return reverseStr(s[1:]) + s[0]

print reverseStr("hoa")