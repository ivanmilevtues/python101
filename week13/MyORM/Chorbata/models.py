import sqlite3
# from Fields import *
from base import BaseMeta


class BaseModel(metaclass=BaseMeta):
    __tablename__ = None

    db = sqlite3.connect(str("BaseModel") + '.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()

    @classmethod
    def create_all_tables(cls):
        for table in cls.registry:
            BaseModel.c.execute(BaseModel.__generate_create_querry(table))
        BaseModel.db.commit()

    @classmethod
    def create_obj(cls, **kwargs):
        # db = sqlite3.connect(str(cls.__name__) + '.db')
        # db.row_factory = sqlite3.Row
        # c = db.cursor()

        insert_kwargs = {}
        for key, value in cls._fields.items():
            if key in kwargs:
                insert_kwargs[key] = kwargs[key]
        query = (BaseModel.__generate_insert_query(cls.__tablename__,
                                                   insert_kwargs))
        print(query)
        BaseModel.c.execute(query)
        BaseModel.db.commit()

    @staticmethod
    def __generate_insert_query(table, kwargs):
        values = 'VALUES('
        query = """INSERT INTO {0}(""".format(table)
        for k, v in kwargs.items():
            query += k + ','
            values += BaseModel.__transform_str(v) + ','
        query = query[:-1]
        query += ')\n'
        values = values[:-1]
        values += ')'
        query += values
        print(query)
        return query

    @classmethod
    def filter(cls, **kwargs):
        query = BaseModel.__generate_select_query(cls.__tablename__, kwargs)
        select_result = BaseModel.c.execute(query)
        return dict(select_result.fetchone())

    @staticmethod
    def __generate_select_query(table_name, kwargs):
        query = """
            SELECT *
            FROM {}
            WHERE""".format(table_name)
        for k, v in kwargs.items():
            query += ' ' + k + '='
            query += BaseModel.__transform_str(v)
            query += 'AND'
        return query[:-3]

    @staticmethod
    def __generate_create_querry(table):
        query = """
            CREATE TABLE {0} (
        """.format(table.__tablename__)
        for name, type_ in table._fields.items():
            query += '\n'
            query += name + ' '
            query += str(type_) + ','
        query = query[:-1]
        query += ')'
        return query

    @staticmethod
    def __transform_str(string):
        if type(string) == str:
            result = '\'' + string + '\''
        else:
            result = string
        return str(result)

# Aristocrat + Material Theme!
