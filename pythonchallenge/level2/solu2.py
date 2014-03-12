import string
data = ''.join([line.rstrip() for line in open('mess.txt')])
print filter(lambda x: x in string.letters, data)
