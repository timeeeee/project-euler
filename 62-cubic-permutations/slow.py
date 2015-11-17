"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from itertools import permutations


class Cubes:
    def __init__(self):
        self.c = 1
        self.cubes = set()
        self.max_cube = 0

    def add_cube(self):
        new_cube = self.c ** 3
        self.cubes.add(new_cube)
        self.max_cube = new_cube
        self.c += 1

    def is_cube(self, n):
        while self.max_cube < n:
            self.add_cube()

        return n in self.cubes


CUBE_COUNTER = Cubes()


def test_cubes():
    c = Cubes()
    tested_cubes = set()
    for x in range(1, 100):
        assert(c.is_cube(x**3))
        tested_cubes.add(x**3)
    for x in range(10000):
        if x not in tested_cubes:
            assert(not(c.is_cube(x)))
            
        
def cubic_permutations(n, number):
    count = 0
    counted_so_far = set()
    for permutation in permutations(str(n)):
        p = int("".join(permutation))
        if p > n and CUBE_COUNTER.is_cube(p) and p not in counted_so_far:
            print "permutation of {} {} is cube".format(n, p)
            counted_so_far.add(p)
            count += 1
        if count == number:
            return True
    return False


def find_cubic_permutations(start_base, number):
    while True:
        n = start_base ** 3
        if cubic_permutations(n, number):
            return n
        start_base += 1


def main():
    print find_cubic_permutations(340, 5)


if __name__ == "__main__":
    main()
