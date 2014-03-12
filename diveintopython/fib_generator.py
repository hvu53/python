def fib(max):
  a, b= 0,1
  while a < max:
    yield a
    a,b = b, b+a

list(fib(100))
for n in fib(1000):
  print(n, end = ' ')