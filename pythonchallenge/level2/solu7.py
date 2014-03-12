import re
data = open("mess.txt").read()
print "".join(re.findall(r'[a-z]', data))
