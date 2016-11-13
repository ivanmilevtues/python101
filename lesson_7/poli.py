from sys import argv


class Derivates:
    def __init__(self):
        self.polinom_list= []

    def split_to_elements(self, polynom):
        self.polinom_list = polinom.split('+')
        for index in range(len(self.polinom_list)):
            self.polinom_list[index] = self.polinom_list[index].split('x^')
        return self.polinom_list

    def solve(self):
        result = []
        for el in self.polinom_list:
            if len(el) == 2:
                if el[0] == '':
                    el[0] = 1
                result.append([int(el[0]) * int(el[1]), (int(el[1]) - 1)])
            elif el[0][-1] == 'x':
                if el[0] == 'x':
                    result.append(1)
                else:
                    result.append(el[0][0:-1])
        return result

    def printer(self):
        result = ''
        result_list = self.solve()
        if not len(result_list):
            return 0
        for el in result_list:
            if type(el) == list:
                result += "{0}*x^{1} + ".format(el[0], el[1])
            else:
                result += "{0} + ".format(el)
        result = result[0: -3]
        return result


def main():
    a = Derivates()
    a.split_to_elements(argv[1])
    print(a.printer())
    #
    # a.split_to_elements("2x^3+x")
    # print(a.printer())
    #
    # a.split_to_elements("5x^4+x^3+3x+3")
    # print(a.printer())
    #
    # a.split_to_elements("1")
    # print(a.printer())

main()
