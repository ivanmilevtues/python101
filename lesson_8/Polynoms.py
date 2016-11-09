class Polynom:

    def __init__(self, polynom_str):
        self.polnom = polynom_str

    def __split(self):
        polynom_members = []
        polynom_members = self.polnom.split('+')
        return polynom_members

    def get_coefficient_power(self):
        result = []
        polynom_members = self.__split()
        for part in polynom_members:
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
    def __init__(self, polynom_dict):
        self.polynom_dict = polynom_dict

    def calc_der(self):
        result = []
        for key, value in self.polynom_dict.items():
            result.append([key*value, key - 1])
        # print(result)
        return sorted(result, key=lambda x:x[1], reverse=True)


class StringModifier:
    def __init__(self, polynom_list):
        self.polynom_list = polynom_list

    def __str__(self):
        result = ''
        for i in self.polynom_list:
            if i[0]:
                if i[1] and i[1] != 1:
                    result += "{0}x^{1}+".format(i[0], i[1])
                elif i[1] == 1:
                    result += "{0}x+".format(i[0])
                else:
                    result += "{0}+".format(i[0])
        return result[:-1]


def main():
    a = Polynom("2x^3+3x+1")
    polynom_dict = a.simplify()
    calc = DerivativeCalculate(polynom_dict)
    polynom_list = calc.calc_der()
    string_mod = StringModifier(polynom_list)
    print(string_mod)
main()
