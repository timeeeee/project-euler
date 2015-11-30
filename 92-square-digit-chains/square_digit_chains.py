def square_digits(n):
    result = 0
    while n:
        n, digit = divmod(n, 10)
        result += digit**2
    return result


def one_or_89(n):
    while n != 1 and n != 89:
        n = square_digits(n)
    return n


def main():
    count = 0
    for n in xrange(1, 10000000):
        if one_or_89(n) == 89:
            count += 1
    print count


if __name__ == "__main__":
    main()
