# a python program
import math

def isprime(n):
    for i in range(2, int(math.floor(math.sqrt(n)))+1):
        if n % i == 0:
            return False
    return True


for i in range(1, 151):
    if isprime(i):
        print(i)
