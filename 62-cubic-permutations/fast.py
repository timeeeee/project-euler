"""
===============================================================================
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
===============================================================================

Strategy: Generate cubes. Keep track of the number of cubes that are
permutations of each other using a dictionary, with the sorted digits of a
number as its key.
"""

def find_cubic_permutations(n):
    c = 1
    cube_counts = dict()
    originals = dict()
    while True:
        cube = c**3
        key = tuple(sorted(str(cube)))
        if key in cube_counts:
            cube_counts[key] += 1
            if cube_counts[key] == n:
                return originals[key]
        else:
            cube_counts[key] = 1
            originals[key] = cube
        c += 1


def main():
    print find_cubic_permutations(5)


if __name__ == "__main__":
    main()
