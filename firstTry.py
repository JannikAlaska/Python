import somemodule

def fib(n=10):
	if n<2:
		return n
	else:
		return fib(n-1)+fib(n-2)

def f(L=None):
	if L is None:
		L = []
	L.append(42)
	return L


var = somemodule.funk2(5,7)
print (var)
