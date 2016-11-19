class Bill:

    def __init__(self, amount):
        if type(amount) != int:
            raise TypeError
        elif amount < 0:
            raise ValueError
        self.amount = amount

    def __str__(self):
        return "A {0}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return self.__int__()


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
        if type(money) == Bill:
            self.money.append(money.amount)
        else:
            self.money += [bill.amount for bill in money]

    def total(self):
        print(self.money)
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
        return sorted(result_dict.items())


def CashDesk_test():
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total())
    # desk.inspect()
    print(desk.inspect())


def batch_bill_test():
    values = [10, 20, 50, 100]
    bills = [Bill(value) for value in values]
    batch = BatchBill(bills)
    print(len(batch))
    print(batch.total())
    for bill in batch:
        print(bill)


def bill_test():
    a = Bill(10)
    b = Bill(5)
    c = Bill(10)
    print(type(int(a)))
    print(str(a))
    print(a)
    print(a == c)
    print(a == b)
    money_holder = {}
    money_holder[a] = 1
    if c in money_holder:
        money_holder[c] += 1
    print(money_holder)


def main():
    # bill_test()
    # batch_bill_test()
    CashDesk_test()

if __name__ == "__main__":
    main()
