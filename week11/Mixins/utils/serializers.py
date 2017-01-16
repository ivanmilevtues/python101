import json
from xml.etree.ElementTree import Element, tostring
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf


class Jsonable:
    serializer_types = (dict,
                        list,
                        int,
                        tuple,
                        float,
                        bool,
                        str,
                        None)

    def before_to_json(self):
        data = {
            'dict': {},
            'classname': self.__class__.__name__
        }
        for k, v in self.__dict__.items():
            if type(v) in self.serializer_types:
                data['dict'][k] = v

            if isinstance(v, Jsonable):
                data['dict'][k] = v.to_before_json()
        return data

    def to_json(self, indent=4):
        return json.dumps(self.before_to_json(), indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        classname = data.get('classname', None)
        if cls.__name__ != classname:
            raise ValueError('{} != {}'.format(cls.__name__, classname))
        return cls(**data['dict'])


class Xmlable:
    def to_xml(self):
        elem = Element(self.__class__.__name__)
        for k, v in self.__dict__.items():
            node = Element(k)
            node.text = str(v)
            elem.append(node)
        return tostring(elem).decode('utf8')

    @classmethod
    def from_xml(cls, xml_string):
        data = bf.data(fromstring(xml_string)).popitem()
        class_name = data[0]
        data = data[1]

        result = {}
        if class_name == cls.__name__:
            for elem in data:
                result[elem] = data[elem].popitem()[1]
                # print(elem, '=>', data[elem])
                # print(elem.popitem())
        else:
            return None
        return cls(**result)
