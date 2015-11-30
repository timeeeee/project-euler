class NDigitNumber(object):
    def __init__(self, n=0, digits=10):
        self.n = n
        self.digits = digits
        self.cutoff()

    def cutoff(self):
        self.n %= 10**self.digits

    def add(self, other):
        self.n += other
        self.cutoff()

    def multiply(self, other):
        self.n *= other
        self.cutoff()

    def subtract(self, other):
        self.n -= other
        self.cutoff()

    def __repr__(self):
        return "NDigitNumber({}, {})".format(self.n, self.digits)

    def __str__(self):
        return str(self.n)


def main():
    num = NDigitNumber(28433, 10)
    for _ in xrange(7830457):
        num.multiply(2)
    num.add(1)
    print num


if __name__ == "__main__":
    main()
