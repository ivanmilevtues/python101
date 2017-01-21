import abc

from validate_email import validate_email


class Field(metaclass=abc.ABCMeta):
    def transform(self, value):
        return value

    @abc.abstractmethod
    def validate(self, value):
        return False


class CharField(Field):
    def transform(self, value):
        return str(value)

    def validate(self, value):
        return True


class EmailField(Field):
    def validate(self, value):
        return validate_email(value)


class DateTimeField(Field):
    def transform(self, value):
        return value.isoformat()

    def validate(self, value):
        return True


class GradeField(Field):
    def transform(self, value):
        return int(value)

    def validate(self, value):
        if value < 0 or value > 12:
            return False
        return True
