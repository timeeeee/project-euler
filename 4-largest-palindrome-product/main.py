# Find the largest palindrome that is the product of 2 3-digit numbers.

def isPalindrome(x):
    string = str(x)
    return "".join(reversed(string)) == string

maximum = 0;
for a in range(111, 1000):
    for b in range(111, 1000):
        product = a * b
        if isPalindrome(product) and product > maximum:
            maximum = product

print maximum
