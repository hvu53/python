import string
data = open('mess.txt').read()
# filter(function, iterable)
print filter(lambda x: x in string.letters, data)
