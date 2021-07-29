#a python program

def isprime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

for i in range(1, 101):
	if isprime(i):
		print(i)



