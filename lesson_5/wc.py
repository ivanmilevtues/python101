import sys
import re


def words():
    with open(sys.argv[2], "r") as f:
        return len(re.findall('\w+', f.read()))


def chars():
    with open(sys.argv[2], "r") as f:
        return sum(1 for char in f.read())


def lines():
    with open(sys.argv[2], "r") as f:
        return sum(1 for char in f.read() if char == '\n')


def wc():
    if sys.argv[1] == "chars":
        return chars()
    elif sys.argv[1] == "words":
        return words()
    elif sys.argv[1] == "lines":
        return lines()


def main():
    print(wc())

if __name__ == "__main__":
    main()
