from string import uppercase

char_values = dict(zip(uppercase, range(1, 27)))


def unquote(string):
    start = 0
    end = len(string) - 1
    start += (string[0] == "\"")
    end -= (string[end] == "\"")
    return string[start:end + 1]


def score(name):
    return sum(char_values[char] for char in name)

if __name__ == "__main__":
    name_file = open("names.txt")
    name_string = name_file.read()
    name_list = map(unquote, name_string.split(","))
    name_list.sort()

    count = 1
    total = 0
    while name_list:
        name = name_list.pop(0)
        total += score(name) * count
        count += 1
    print total
