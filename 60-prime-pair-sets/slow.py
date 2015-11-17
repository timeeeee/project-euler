"""
Project Euler Problem 60: Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
these four primes, 792, represents the lowest sum for a set of four primes
with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

from itertools import combinations
from sys import stdout


class Primes(object):
    def __init__(self):
        self.ordered_primes = [2, 3]
        self.prime_dict = {2: True, 3: True}
        self.number_to_check = 5
        self.num_primes = 2
        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        prime = self[self.index]
        self.index += 1
        return prime

    def is_prime(self, n):
#        print "check is {} prime?".format(n)
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # Check cache- may or may not help depending on how common hits are
        if n in self.prime_dict:
            return self.prime_dict[n]
        """
        # No easy answer- check primes we already know then other factors
        for prime in self.ordered_primes:
            if n % prime == 0:
                self.prime_dict[n] = False
                return False

        # turns out simple iterative is faster???
        """
        factor = 3
        while factor ** 2 < n:
            if n % factor == 0:
                self.prime_dict[n] = False
                return False
            factor += 2

        # Factor is now >= sqrt(n)- is n = factor**2
        if factor ** 2 == n:
            self.prime_dict[n] = False
            return False

        # n has no factors- it's prime!
        self.prime_dict[n] = True
        return True

    def __getitem__(self, n):
        """Get (n+1)th prime"""
#        print "get primes[{}]".format(n)
        while self.num_primes <= n:
            self.add_prime()

        return self.ordered_primes[n]

    def add_prime(self):
#        print "add prime!"
        found_prime = False
        while not found_prime:
            if self.is_prime(self.number_to_check):
                found_prime = True
                self.ordered_primes.append(self.number_to_check)
                self.num_primes += 1
            self.number_to_check += 2


def index_generator(n):
    """Generate all possible sets of n ints, starting low"""
    maximum = n - 1
    while True:
        for c in combinations(range(maximum), n - 1):
            yield c + (maximum,)

        maximum += 1
    

def is_prime_pair_set(prime_list, prime_object):
    for str_x, str_y in combinations(map(str, prime_list), 2):
        if not (prime_object.is_prime(int(str_x + str_y)) and
                prime_object.is_prime(int(str_y + str_x))):
            return False
    return True


def prime_pair_set(length):
    prime_object = Primes()
    old_max = -1
    for indices in index_generator(length):
        prime_list = [prime_object[n] for n in indices]
        if prime_list[-1] > old_max:
            old_max = prime_list[-1]
            print "max = {}".format(old_max)
            stdout.flush()
        if is_prime_pair_set(prime_list, prime_object):
            return prime_list


def main():
    primes = Primes()
    print prime_pair_set(5)
#    print is_prime_pair_set([3, 7, 109, 673], primes)


if __name__ == "__main__":
    main()
