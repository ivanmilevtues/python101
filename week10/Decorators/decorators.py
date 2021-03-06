# Decorators
import time
from functools import wraps
import re
from datetime import datetime


def accepts(*types):
    def get_func(func):
        def decorated(*args):
            for ind in range(len(args)):
                if not isinstance(args[ind], types[ind]):
                    raise TypeError
            return func(*args)
        return decorated
    return get_func


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


def encrypt(num):
    def get_func(func):
        def char_shift(*args):
            sentence = list(func())
            result = ''
            for indx in range(len(sentence)):
                if re.search('[a-z]|[A-Z]', sentence[indx]):
                    # print(sentence[indx])
                    # sentence[indx] = ((ord(sentence[indx]) - ord('a') + num)) % 26 + ord('a')
                    # print(sentence[indx])
                    # print(((ord(sentence[indx]) - ord("a") + num)) % 26)
                    sentence[indx] = chr(ord(sentence[indx]) + num)
                # elif re.search('[A-Z]', sentence[indx]):
                #     sentence[indx] = chr(((ord(sentence[indx]) +
                #                         num - ord('A'))) % 26 +
                #                         ord(sentence[indx]))
            for char in sentence:
                result += char
            return result
        return char_shift
    return get_func


def log(file):
    def get_func(func):
        @wraps(func)
        def decorated(*args, **kvargs):
            with open(file, "a") as f:
                f.write(str(datetime.now()))
            return func(args, kvargs)
        return decorated
    return get_func


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

    
def performance(file):
    def get_func(func):
        def decorated(*args, **kvargs):
            start_time = time.time()
            func()
            end_time = time.time()
            with open(file, "a") as f:
                f.write(str(end_time - start_time))
            f.close()
        return decorated
    return get_func

@performance('log.txt')
def main():
    # print(say_hello("Ivan"))
    # print(deposit("Kik", '3'))
    print(get_low(2))
    # print(say_hello(1))


if __name__ == '__main__':
    main()
