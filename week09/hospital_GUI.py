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


def update_doctor(doctor_id, new_info):
    update_querry = """
                    UPDATE doctors
                    SET FIRSTNAME="{0}", LASTNAME = "{1}" 
                    WHERE ID = {2}
                    """.format(new_info[0], new_info[1],
                               doctor_id)

    c.execute(update_querry)


def update_patient(patient_id, new_info):
    update_querry = """
                    UPDATE patients
                    SET FIRSTNAME = "{0}", LASTNAME = "{1}", AGE = {2}, GENDER = "{3}", DOCTOR = {4}
                    WHERE ID = {5};
                    """.format(new_info[0], new_info[1], new_info[2],
                               new_info[3], new_info[4], patient_id)

    c.execute(update_querry)


def update_hospital(hospital_id, new_info):
    update_querry = """
                    UPDATE hospital_stay
                    SET ROOM = {0}, STARTDATE = "{1}", ENDDATE = "{2}", INJURY = "{3}", PATIENT = {4}
                    WHERE ID = {5};
                    """.format(new_info[0], new_info[1], new_info[2], new_info[3], new_info[4],
                               hospital_id)

    c.execute(update_querry)


def delete_person(person_id, table):
    delete_query = """
                   DELETE FROM {0}
                   WHERE ID = {1};
                   """.format(table, person_id);

    c.execute(delete_query)


def patients_of_doctor(doctor_id):
    select_querry = """
                    SELECT p.ID, p.FIRSTNAME, p.LASTNAME, p.AGE, p.GENDER
                    FROM doctors as d, patients as p
                    WHERE d.ID = {0} AND d.ID= p.DOCTOR;
                    """.format(doctor_id)

    patients_list = c.execute(select_querry)
    
    table = PrettyTable()
    for row in patients_list:
        table.add_row(row)
    print(table)


def list_patients_in_date_range(start_date, end_date):
    select_querry = """
                    SELECT p.ID, p.FIRSTNAME, p.LASTNAME, p.AGE, p.GENDER
                    FROM hospital_stay as h, patients as p
                    WHERE p.ID = h.PATIENT AND h.STARTDATE > "{0}" AND h.ENDDATE < "{1}"
                    """.format(start_date, end_date)
    patients_list = c.execute(select_querry)

    table = PrettyTable()
    for row in patients_list:
        table.add_row(row)
    print(table)


def main():
    insert_doctor(["Milcho", "Milev"])
    insert_patient(["Kikomir", "Kikom", 3, "M", 3])
    
    update_doctor(1, ["Nedlecho", "Bogdanov"])
    update_patient(1, ["Zaprqnko", "Ivanov", 60, "M", 1])
    update_hospital(1, [3, "2016-11-11", "2016-12-12", "Cancer", 1])
    list_patients_in_date_range("2016-01-01", "2017-12-30");
    # list_people("patients")
    # list_people("doctors")
    
    # delete_person(2, "patients")
    # delete_person(2, "doctors")
    
    # list_people("patients")
    # list_people("doctors")

    patients_of_doctor(2)

    # db.commit()


if __name__ == '__main__':
    main()
