if __name__ == "__main__":
    infile = open("data.txt")
    sumInt = sum(int(line) for line in infile)
    print str(sumInt)[:10]
