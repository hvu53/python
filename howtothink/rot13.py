import string
def rot13(msg):
	alphabet = string.ascii_lowercase
	encrypted = ''
	for ch in msg:
		if ch == ' ':
			encrypted += ' '
		else:
			rotated_index = alphabet.index(ch) + 13
			if rotated_index < 26:
				encrypted += alphabet[rotated_index]
			else:
				encrypted += alphabet[rotated_index % 26]
	return encrypted

print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('since rot thirteen is symmetric you should see this message')))
