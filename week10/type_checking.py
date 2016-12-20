import sys
import re


def check_name(func_name):
    if re.search("\W+", func_name):
        return False

    if not func_name.islower():
        return False
    return True


def validate(func_def):
    func_def = func_def[:-1]
    func_elements = func_def.split(' ')

    if not check_name(func_elements[0]):
        return False

    for el in func_elements:
        if el != '::' and el != '->' and el != '.':
            if re.search("\W+|\[\]", el):
                print(el)
                return False
    return True


def validate_file(inpt):
    # input_str = inpt[0].split('\n')
    # print(input_str)

    for element in inpt:
        if element != '\n':
            if not validate(element):
                return False
    return True


def check_type_rule(inpt):
    for el in inpt:
        if '.' in el:
            functions = el.split(' . ')
            if functions[-1][-1] == '\n':
                functions[-1] = functions[-1][:-1]

    functions = functions[::-1]
    input_types = []
    res = []
    for i in inpt:
        print(i)
        input_types.append(i.split('-> '))

    for f in functions:
        for i in inpt:
            if i[0] == f:
                print("K : " + i[2])
                res.append(i)
    print(res)


def main():
    inpt = list(sys.stdin)
    print(validate_file(inpt))
    print(check_type_rule(inpt))
    print(inpt)

if __name__ == '__main__':
    main()
