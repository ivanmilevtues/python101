from fileds import Field
from datetime import datetime


class SerializerMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = {}
        for attr, value in clsdict.items():
            if isinstance(value, Field):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_declared_fields'] = fields
        clsobj = super().__new__(cls, name, bases, clsdict)

        return clsobj


class Serializer(metaclass=SerializerMeta):
    def __init__(self, instatnce):
        self._object = instatnce
        self._called_validation = False

    def is_valid(self):
        valid = True

        for field_name, field in self._declared_fields.items():
            if not field.validate(getattr(self._object, field_name)):
                valid = False
                break

        self._called_validation = True

        return valid

    @property
    def data(self):
        if not self._called_validation:
            raise Exception('.is_valid() wasn\'t called!')

        return  { field_name: field.transform(getattr(self._object, field_name))
                  for field_name, field in self._declared_fields.items()}
