"""
===============================================================================
The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
===============================================================================
"""

def count_digits(n):
    return len(str(n))


def count_power_digits():
    power_numbers = set()
    # 10**n has n + 1 digits: we can stop at 9
    for n in range(1, 10):
        power = 1
        # Stop checking powers once power exceeds digits
        while count_digits(n**power) >= power:
            if count_digits(n**power) == power:
                power_numbers.add(n**power)
            power += 1
    print power_numbers
    return len(power_numbers)


def main():
    print count_power_digits()


if __name__ == "__main__":
    main()
