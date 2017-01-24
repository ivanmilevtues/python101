from Fields import Column


class BaseMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = {}
        for attr, value in clsdict.items():
            if isinstance(value, Column):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_fields'] = fields

        if not hasattr(cls, 'registry'):
            cls.registry = set()

        clsobj = super().__new__(cls, name, bases, clsdict)
        if clsobj.__tablename__:
            cls.registry.add(clsobj)
        return clsobj
