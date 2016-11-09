import sys
import os


def duhs():
    size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
            for f in filenames:
                file_path = os.path.join(dirpath, f)
                size += os.path.getsize(file_path)
        return (size // (10**7) / 100)
    except FileNotFoundError as error:
        print(error)


def main():
    print(duhs())


if __name__ == '__main__':
    main()
