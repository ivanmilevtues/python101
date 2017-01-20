from Xlib import display
import zipfile
import getch
import random
import string
import os
# import Xlib.display as display


def chain(iterable_one, iterable_two):
    iter_one = iter(iterable_one)
    iter_two = iter(iterable_two)
    try:
        while True:
            yield(next(iter_one))
    except StopIteration:
        try:
            while True:
                yield(next(iter_two))
        except StopIteration:
            pass


# Better solution:
# def chain(iterable_one, iterable_two):
#     for el in iterable_one:
#         yield el
#     for el in iter_two:
#         yield el

def compress(iterable, mask):
    for i in range(len(mask)):
        if mask[i]:
            yield iterable[i]


def cycle(iterable):
    while True:
        for i in iterable:
            yield i


def book_reader(path="Book.zip"):
    with zipfile.ZipFile(path, "r") as myzip:
        chapter_names = myzip.namelist()
        for i in chapter_names:
            with myzip.open(i, "r") as curr_file:
                line = curr_file.readline().decode('utf-8')
                while line:
                    if line.startswith('#'):
                        yield line
                        # yield curr_file.readline().decode('utf-8')
                    line = curr_file.readline().decode('utf-8')


def generate_word():
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))

    return ''.join(random.choice(chars) for i in range(random.randint(0, 30)))


def generate_book(chapters, length):
    for ch_num in range(1, chapters + 1):
        yield("# Chapter {0}\n".format(ch_num))
        for _ in range(length):
            yield generate_word() + ' '
        yield("\n")


def write_book(chapters, length):
    with open("MyBook.txt", "w") as f:
        for line in generate_book(chapters, length):
            f.write(line)
    f.close()
    with zipfile.ZipFile('test.zip', 'w') as mz:
        mz.write('MyBook.txt')


def mousepos():
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]


def main():
    while True:
        ms = mousepos()
        if ms[0] == 0 and ms[1] == 0:
            print('\a')
        # print(type(mousepos()[0]))
#     print(list(chain(range(0, 3), range(0, 5))))
#     print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
#     chapters = book_reader()
#     for chap in chapters:
#         while True:
#             a = getch.getch()
#             if a == ' ':
#                 break
#         print(chap)

#     write_book(3, 100)
#     chapters = book_reader("test.zip")
#     for chap in chapters:
#         while True:
#             a = getch.getch()
#             if a == ' ':
#                 break
#         print(chap)


if __name__ == '__main__':
    main()
