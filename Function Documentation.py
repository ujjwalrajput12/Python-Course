#Function Documentation
def fib(n):
	a,b = 0,1
	while a< n:
		print(a,end=' ')
		a,b =b, a+b
		print()
print(fib(2000))



#2.Row And column both
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


#3.Column wise
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

#4.

