import sys


def multi_file_cat():
    for i in range(1, len(sys.argv)):
        read_one(sys.argv[i])


def read_one(path):
    with open(path, "r") as f:
        print(f.read())
    f.closed


def main():
    multi_file_cat()


if __name__ == '__main__':
    main()
