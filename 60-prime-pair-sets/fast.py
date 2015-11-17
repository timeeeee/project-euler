"""
===============================================================================
Project Euler Problem 60: Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
these four primes, 792, represents the lowest sum for a set of four primes
with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
===============================================================================

This solution builds possible pair sets from the bottom up. For each new prime,
add it as a new possible set, then find all sets so far that it fits into and
create a new set from those with this prime added.
"""

def is_prime(n):
    """Assuming n is odd, is it prime?"""
    factor = 3
    while factor**2 < n:
        if n % factor == 0:
            return False
        factor += 2
    return not(factor**2 == n)


def prime_generator():
    """Generate primes except for 2 and 5"""
    yield 3
    n = 7
    while True:
        if is_prime(n):
            yield n
        n += 2


def prime_pair(x, y):
    str_x = str(x)
    str_y = str(y)
    return is_prime(int(str_x + str_y)) and is_prime(int(str_y + str_x))


def prime_pair_set(length):
    primes = []  # all primes processed so far
    partial_sets = []  # list of tuples, all sets built so far
    for prime in prime_generator():
        print "now we are building {} sets. adding prime {}...".format(
            len(partial_sets), prime)
        # Find every smaller prime that this prime pairs with
        pairs = set(p for p in primes if prime_pair(p, prime))

        # Find which partial sets match this prime
        for partial_set in partial_sets:
            if pairs.issuperset(partial_set):
                if len(partial_set) == length - 1:
                    return partial_set + (prime,)
                partial_sets.append(partial_set + (prime,))
        partial_sets.append((prime,))
        primes.append(prime)


def main():
    print prime_pair_set(5)


if __name__ == "__main__":
    main()
