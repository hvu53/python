pirates = {}
pirates['sir'] = 'matey'
pirates['hotel'] = 'fleabag inn'
pirates['student'] = 'swabbie'
pirates['boy'] = 'matey'
pirates['restaurant'] = 'galley'

sentence = input("Please enter a sentence in English:")

psentence = []
words = sentence.split()

for word in words:
	if word in pirates:
		psentence.append(pirates[aword])
	else:
		psentence.append(aword)

print (" ").join(psentence)