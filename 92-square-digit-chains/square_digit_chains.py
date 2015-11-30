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


def slow():
    count = 0
    for n in xrange(1, 10000000):
        if one_or_89(n) == 89:
            count += 1
    print count


def one_or_89_with_cache(n, cache):
    path = []
    while True:
        if n in cache:
            for num in path:
                cache[num] = cache[n]
            return cache[n]
        path.append(n)
        n = square_digits(n)


def fast():
    solution_cache = {1: 1, 89: 89}
    count = 0
    for n in xrange(1, 10000000):
        if one_or_89_with_cache(n, solution_cache) == 89:
            count += 1
    print count
    

if __name__ == "__main__":
    fast()
