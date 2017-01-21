from datetime import datetime

from fileds import CharField, EmailField, DateTimeField, GradeField
from Serializer import Serializer


class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()


class Student(Person):
    def __init__(self, grade, *args):
        self.grade = grade
        super().__init__(*args)


class PersonSerializer(Serializer):
    name = CharField()
    email = EmailField()
    created_at = DateTimeField()


class StudentSerializer(Serializer):
    grade = GradeField()
    name = CharField()
    email = EmailField()
    created_at = DateTimeField()


def main():
    p = Person('Mitko', 'miteto@k.com')
    s = PersonSerializer(instatnce=p)

    st = Student(12, 'Uchecnichko', 'uchenik@daskalo.com')
    ss = StudentSerializer(st)
    # print(s.__dict__)
    s.is_valid()
    # print(s.is_valid())
    print(s.data)
    # print(ss.is_valid())
    ss.is_valid()
    print(ss.data)


if __name__ == '__main__':
    main()
