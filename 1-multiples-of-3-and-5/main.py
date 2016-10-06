# Sum of all numbers less than 1000 that are divisible by 3 or 5

print sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
