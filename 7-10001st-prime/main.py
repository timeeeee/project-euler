# What is the 10001st prime number?


def isPrime(x):
    factor = 3
    while (factor**2 <= x):
        if x % factor == 0:
            return False
        factor += 2
    return True

count = 1
n = 1
while count < 10001:
    n += 2
    if isPrime(n):
        count += 1

print n
