import collections
data = ''.join([line.rstrip() for line in open('mess.txt')])

OCCURRENCES = collections.OrderedDict()
for c in data: OCCURRENCES[c] = OCCURRENCES.get(c,0) + 1
avgOC = len(data) // len(OCCURRENCES)
print ''.join([c for c in OCCURRENCES if OCCURRENCES[c] < avgOC])
