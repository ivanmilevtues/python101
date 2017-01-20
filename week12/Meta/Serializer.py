from datetime import datetime


class SerializerMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = {}
        print(name)
        for attr, value in clsdict.items():
            if not callable(value) and not attr.startswith('__'):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_declared_fields'] = fields
        clsobj = super().__new__(cls, name, bases, clsdict)

        return clsobj


class Serializer(metaclass=SerializerMeta):
    def __init__(self):
        for attr, value in self._declared_fields.items():
            setattr(self, attr, value)


class EmailField():
    pass


class CharField():
    pass


class DateTimeField():
    pass


class Comment(object):
    def __init__(self, email, content, created_at=None):
        self.email = email
        self.content = content

        if created_at is None:
            created_at = datetime.now()

        self.created_at = created_at


class CommentSerializer(Serializer):
    email = EmailField()
    content = CharField()
    created_at = DateTimeField()

    def __init__(self, comment):
        self.comment = comment


comment = Comment(email='radorado@hakbulgaria.com',
                  content='wie naistina li hakvate?')

serializer = CommentSerializer(comment)

print(vars(serializer))
# print(serializer.is_valid()) # True
# print(serializer.data)
"""
{
  "email": "radorado@hackbulgaria.com",
  "content": "wie naistina li hakvate?",
  "created_at": "'2017-01-20T13:43:10.704846'"
}
"""
