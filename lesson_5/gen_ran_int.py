from random import randint
import sys


def write_file():
    with open(sys.argv[1], "w") as f:
        for i in range(100):
            f.write(str(randint(1, 1000)))
            f.write(" ")


def main():
    write_file()


if __name__ == '__main__':
    main()
