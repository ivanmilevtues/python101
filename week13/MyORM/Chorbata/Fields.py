import abc


class Column(metaclass=abc.ABCMeta):
    def transform(self, *args, **kwargs):
        return value

    @abc.abstractmethod
    def validate(self, *args, **kwargs):
        return False


class PKColumn(Column):
    def __init__(self):
        self.value = 0

    def transform(self):
        return int(self.value)

    def validate(self):
        return type(self.value) == int

    def __str__(self):
        return 'INTEGER PRIMARY KEY AUTOINCREMENT'


class TextColumn(Column):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k == 'max_length':
                self.max_length = v

    def transform(self, string):
        return str(string)

    def validate(self, string):
        return type(string) == str and self.max_length <= len(self.string)

    def __str__(self):
        return 'TEXT'


class IntegerColumn(Column):
    def __init__(self, number):
        self.number = number

    def transform(self):
        return self.number

    def validate(self):
        return type(self.number) == int

    def __str__(self):
        return 'INTEGER'
