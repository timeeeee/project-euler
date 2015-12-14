"""
Find the line number of the base/exponent pair with the largest result

Strategy: a^m > b^n => log(a^m) > log(b^n) => m * log(a) > n * log(b)
"""

from math import log
from sys import argv

def main():
    if len(argv) == 1:
        print ("Find the line number of the base/exponent pair with the "
               "largest result.\n"
               "Usage: python main.py <input_file>")
        exit(1)
        
    with open(argv[1]) as f:
        pairs = [map(int, line.split(',')) for line in f]
    log_of_exp, line_number  = max(
        (log(base) * exp, num + 1) for num, (base, exp) in enumerate(pairs))
    print line_number


if __name__ == "__main__":
    main()
    
    
