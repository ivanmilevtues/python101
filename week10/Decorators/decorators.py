def accepts(name, *args):
    def get_func(func):
        def decorated(name, *args):
            if not isinstance(name, str):
                raise TypeError
            return func(name, *args)
        return decorated
    return get_func


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


print(say_hello("Ivan"))
print(deposit("Kik", 3))
# print(say_hello(1))
