import re

f = open("alice.txt", "r")

count = {}
for line in f:
	words = line.split()
	for word in words:

		# remove puntuaion
		word = re.sub(r'[^\w\s]','',word)
		# ignore case
		word = word.lower()
		#igmore number

		if word.isalpha():
			if word in count:
				count[word] +=1
			else:
				count[word] =1

keys = count.keys()
keys.sort()

longest = 0
longest_word = ''
for i in keys:
	if count[i] > longest:
		longest = count[i]
		longest_word = i

print ('longest: ' + str(longest_word) + " " + str(longest))
out = open("alice_count.txt","w")

for word in keys:
	out.write(word+ ": " +str(count[word]))
	out.write('\n')

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")

# exclude = set(string.punctuation)
# s = ''.join(ch for ch in s if ch not in exclude)