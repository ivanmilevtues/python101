import re


def args_validate(*args):
    print("Someone here")

    def get_func(func):
        def checker(*args):
            print(type(args), ' -> ', args)
            if type(args) is list:
                if len(args) > 2:
                    print("Too much arguments given!")
                    return False
                for indx in range(len(args)):
                    if indx == 0:
                        if not re.match(r"\d+", args[indx]):
                            print("First argument has wrong format!")
                            return False
                    if indx == 1:
                        if not re.match(r"\[\d+-\d+-\d+\]+", args[indx]):
                            print("Second argument has wrong format!")
                            return False
            return func()
    return get_func
