import os

def factorielRecursif(n):
	if(n == 0):
		return 1
	else:
		return n * factorielRecursif(n-1)

print(factorielRecursif(10))

