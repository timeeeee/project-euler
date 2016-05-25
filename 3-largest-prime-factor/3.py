"""What is the largest prime factor of the number 600851475143?"""


def prime_factors(n):
    factors = []
    factor = 3
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n /= factor
        factor += 2
    return factors


def test_prime_factors():
    primes = [3, 5, 7, 11, 13, 17, 19, 23]
    for prime in primes:
        assert prime_factors(prime) == [prime]

    assert set(prime_factors(13195)) == {5, 7, 13, 29}


if __name__ == "__main__":
    test_prime_factors()
    print prime_factors(600851475143)[-1]
