"""
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def gcd(a, b):
    """Find the greatest common denominator of a and b using euclid's
    algorithm.
    """
    if a < b:
        a, b = b, a

    while b > 0:
        quotient, remainder = divmod(a, b)
        a, b = b, remainder

    return a


def lcm(a, b):
    """Find the least common multiple of a and b."""
    return a * b / gcd(a, b)


def smallest_number_div_by_1_to(n):
    multiple = 1
    for x in range(2, n + 1):
        multiple = lcm(multiple, x)
    return multiple


if __name__ == "__main__":
    print smallest_number_div_by_1_to(20)
