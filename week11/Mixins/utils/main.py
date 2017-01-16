from serializers import *


class Panda(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            

if __name__ == '__main__':
    a = Panda(name="mitov", smth="thi", what="tjasd")
    p = a.to_json()
    p1 = Panda.from_json(p)
    print(p1.name)
    # print(a.to_xml())
    b = a.to_xml()
    b1 = Panda.from_xml(b)
    print(b1.name)
