# Cheating solution

# sum of digits of the number 2^n
def sumOfDigits(n):
    return sum(map(int, str(2**n)))

if __name__ == "__main__": 
    print sumOfDigits(1000)
