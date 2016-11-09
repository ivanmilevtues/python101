class Polinom:

    def __init__(self, polinom_str):
        self.polnom = polinom_str

    def __split(self):
        polinom_members = []
        polinom_members = self.polnom.split('+')
        return polinom_members

    def get_coefficient_power(self):
        result = []
        polinom_members = self.__split()
        for part in polinom_members:
            if 'x' not in part:
                continue
            sub_part = part.split('x^')
            result.append(sub_part)
        for i in range(len(result)):
            # print(result[i][0])
            if 'x' in result[i][0]:
                result[i] = [result[i][0][0], 1]
            if result[i][0] == '':
                result[i][0] = 1
        # print(result)
        return result

    def simplify(self):
        result_dict = {}
        result = self.get_coefficient_power()
        for i in result:
            if int(i[1]) not in result_dict:
                result_dict[int(i[1])] = 0
            result_dict[int(i[1])] += int(i[0])
        return result_dict


class DerivativeCalculate:
    def __init__(self, polinom_dict):
        self.polinom_dict = polinom_dict

    def calc_der(self):
        result = []
        for key, value in self.polinom_dict.items():
            result.append([key*value, key - 1])
        # print(result)
        return sorted(result, key=lambda x:x[1], reverse=True)


class StringModifier:
    def __init__(self, polinom_list):
        self.polinom_list = polinom_list

    def __str__(self):
        result = ''
        for i in self.polinom_list:
            if i[0]:
                if i[1] and i[1] != 1:
                    result += "{0}x^{1}+".format(i[0], i[1])
                elif i[1] == 1:
                    result += "{0}x+".format(i[0])
                else:
                    result += "{0}+".format(i[0])
        return result[:-1]


def main():
    a = Polinom("2x^3+3x+1")
    polinom_dict = a.simplify()
    calc = DerivativeCalculate(polinom_dict)
    polinom_list = calc.calc_der()
    string_mod = StringModifier(polinom_list)
    print(string_mod)
main()
