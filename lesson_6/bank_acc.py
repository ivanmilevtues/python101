class Bill:
    def __init__(self, amount):
        self.amount = amount
        if amount < 0:
            raise ValueError
        elif type(amount) != int:
            raise TypeError

    def __str__(self):
        return "A {0}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return int(self)


class BatchBill:
    def __init__(self, bill_list):
        self.bills = bill_list

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum(el.amount for el in self.bills)

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:
    def __init__(self):
        self.money = []

    def take_money(self, money):
        # print(type(money) == Bill)
        if type(money) == Bill or isinstance(money, Bill):
            self.money.append(money.amount)
        elif type(money) == BatchBill or isinstance(money, BatchBill):
            self.money += [bill.amount for bill in money]

    def total(self):
        return sum(a for a in self.money)

    def inspect(self):
        result_dict = {}
        for i in self.money:
            if i in result_dict:
                result_dict[i][1] += 1
            else:
                result_dict[i] = []
                result_dict[i].append(str(i) + "$ bills - ")
                result_dict[i].append(1)
        result_dict = sorted(result_dict.items())
        # print(type(result_dict))
        for i in result_dict:
            print(i[1][0] + str(i[1][1]))


def main():
    # a = Bill(10)
    # b = Bill(5)
    # c = Bill(10)
    # print(a)
    # print(a == b)
    # print(a == c)
    # money_holder = {}
    # money_holder[a] = 1
    # values = [10, 20, 50, 100]
    # bills = [Bill(value) for value in values]
    #
    # batch = BatchBill(bills)
    #
    # for bill in batch:
    #     print(bill)
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total()) # 390
    desk.inspect()

if __name__ == '__main__':
    main()
