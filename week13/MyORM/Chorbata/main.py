from Fields import PKColumn, IntegerColumn, TextColumn
from models import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    id = PKColumn()
    name = TextColumn(max_length=100)
    age = IntegerColumn(number=20)


class Student(BaseModel):
    __tablename__ = 'student'
    email = TextColumn()
    shirt_size = IntegerColumn(number=1)


BaseModel.create_all_tables()
User.create_obj(name='Ceci', age=44)
# print(BaseModel.registry)
# s = Student()
# print(User.__dict__)
# Create record in table
# User.create_obj(name="Rosi", age=22)

# Return dict with object
print(User.filter(name="Ceci"))
