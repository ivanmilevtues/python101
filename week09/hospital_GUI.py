from prettytable import PrettyTable
import sqlite3


DB_NAME = "hospital.db"
db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def list_to_values(l):
    values = ''
    for el in l:
        values += "\""
        values += str(el)
        values += "\", "
    return values[:-2]


def list_people(tble):
    querry = """SELECT * FROM {0} """.format(tble)
    result = c.execute(querry)
    table = PrettyTable()
    # table.field_names = ["FIRSTNAME", "LASTNAME"]
    for row in result:
        table.add_row(row)
    print(table)


def insert_patient(info):
    info_str = list_to_values(info)
    insert_querry = """INSERT INTO patients (FIRSTNAME, LASTNAME, AGE, GENDER, DOCTOR)
                       VALUES({0})""".format(info_str)

    c.execute(insert_querry)


def insert_doctor(info):
    info_str = list_to_values(info)
    insert_querry = """INSERT INTO doctors (FIRSTNAME, LASTNAME)
                       VALUES ({0})""".format(info_str)

    c.execute(insert_querry)


def main():
    insert_doctor(["Milcho", "Milev"])
    insert_patient(["Kikomir", "Kikom", 3, "M", 3])
    list_people("patients")
    list_people("doctors")
    # db.commit()

if __name__ == '__main__':
    main()
