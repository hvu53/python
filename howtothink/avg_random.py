def max(l):
	maxi = 0
	for i in l:
		if i > maxi:
			maxi =3
	return maxi

def gen_ran(n):
	l = []
	for i in range(100):
		l.append(random.randint(0,1000))
	return l