#a python program

def isprime(n):
	for i in range(2,int(n/2)+1):
		if n%i == 0:
			return False
	return True

for i in range(1, 151):
	if isprime(i):
		print(i)



