"""
Strategy: If it ends in a 0, must be multiple of 10, so must also be a multiple
of 100- find int whose square has form 1_2_3_4_5_6_7_8_9. For the last digit of
n^2 to be 9, last digit of n must be 3 or 7 so only test those.
sqrt(10203040506070809) = 101010101.010101 so only test above 101010101.
sqrt(19293949596979899) = 138902662.31062636 so only test up to 138902662.
"""


def has_form(n):
    for digit in range(9, 0, -1):
        if n % 10 != digit:
            return False
        n, _ = divmod(n, 100)
    return True


def test_has_form():
    from random import choice
    from string import digits

    # Test False
    print "test True:"
    for _ in xrange(50):
        num = int("".join(choice(digits) for _ in xrange(17)))
        print "  has_form({}): {}".format(num, has_form(num))

    # Test True
    print "test False:"
    for _ in xrange(50):
        num = int("1{}2{}3{}4{}5{}6{}7{}8{}9".format(*[
            choice(digits) for _ in xrange(8)]))
        print "  has_form({}): {}".format(num, has_form(num))


def find_sqrt_1_2_3_4_5_6_7_8_9_0():
    for tens in range(1010100, 138902662, 10):
        if has_form((tens + 3)**2):
            return (tens + 3) * 10
        if has_form((tens + 7)**2):
            return (tens + 7) * 10
    raise Exception("didn't find it!")


if __name__ == "__main__":
    n = find_sqrt_1_2_3_4_5_6_7_8_9_0()
    print "{}^2 = {}".format(n, n**2)
