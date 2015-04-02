"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def sumOfDivisors(x):
    total = 1
    factor = 2
    while factor**2 < x:
        if x % factor == 0:
            total += factor + x / factor
        factor += 1
    if factor**2 == factor:
        total += factor
    return total

if __name__ == "__main__":
    divisorSums = map(sumOfDivisors, range(1,10000))
    total = 0
    for x in range(1,10000):
        buddy = divisorSums[x - 1]
        if buddy > x and buddy < 10000 and divisorSums[buddy - 1] == x:
            total += x + buddy
    print total
