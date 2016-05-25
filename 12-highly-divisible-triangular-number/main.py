# What is the first triangular number to have more than 500 divisors?

def divisorCount(x):
    count = 0
    divisor = 1
    while divisor ** 2 < x:
        if x % divisor == 0: count += 2
        divisor += 1
    if divisor ** 2 == x: count += 1
    return count

def TriangleGenerator():
    count = 1
    triangle = 0
    while True:
        triangle += count
        count += 1
        yield triangle

def triangle500div():
    triangles = TriangleGenerator()
    for triangle in triangles:
        divisors = divisorCount(triangle)
        if divisors > 500:
            return triangle


if __name__ == "__main__":
    print triangle500div()

# Takes 45 seconds on my netbook, what the heck
