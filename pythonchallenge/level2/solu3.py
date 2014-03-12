data = open("mess.txt").read()
import string
trans = string.maketrans(string.printable, string.printable)
result = string.translate(data, trans, string.punctuation+'\n')
print result
