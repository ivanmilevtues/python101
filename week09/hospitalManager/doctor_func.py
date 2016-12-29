import sqlite3

from queries import *
from user_func import *
from doctor import Doctor
from prettytable import PrettyTable


def menu(doc):
    options = '''
Welcome {0}, you are logged in as Doctor!
1. Register
2. Log into the system
3. List all patients
4. Add hour for visitation
5. Delete free hours of visitation
6. See the room and duratioin of hospital stays per patient
7. Log out
8. Exit
'''.format(doc.name)
    print(options)
    return True


def list_patients(doc):
    patients = c.execute(SELECT_DOCTOR_PATIENTS, [doc.get_id(), ])
    patient_table = PrettyTable()
    patient_table.field_names = ["Patients"]
    for patient in patients:
        patient_table.add_row([patient['USERNAME']])
    print(patient_table)
    return True


def add_visitiation_hour(doc):
    doc_id = doc.get_id()
    patient = input("Patient name: ")
    start_time = input("Start hour: ")
    patients = c.execute(SELECT_DOCTOR_PATIENTS, [doc_id, ])
    for pat in patients:
        print("Searching for patient...")
        if pat['USERNAME'] == patient:
            print("Patient found. Adding visitation...")
            print(pat['ID'])
            c.execute(INSERT_VISITATION_HOUR, [
                      pat["ID"], doc_id, start_time, ])
            print("Visitation hour added!")
            break
    db.commit()
    return True


def delete_visitation_hour(*args):
    delete_hour = input("The start hour you want to delete:")
    c.execute(DELETE_VISITATION_HOUR, [delete_hour, ])
    db.commit()
    return True


def get_hospital_stay(doc):
    patient_id = input("Input the patient id: ")
    hosp_stay = c.execute(GET_HOSPITAL_STAY, [patient_id, ])

    hosp_table = PrettyTable()
    hosp_table.field_names = ['STARTDATE', 'ENDDATE', 'INJURY']

    for stay in hosp_stay:
        hosp_table.add_row([stay['STARTDATE'], stay['ENDDATE'],
                            stay['INJURY']])

    print(hosp_table)
    return True


DOCTOR_OPTIONS = {
    1: register,
    2: login,
    3: list_patients,
    4: add_visitiation_hour,
    5: delete_visitation_hour,
    6: get_hospital_stay,
    7: logout,
    8: exit
}


def doctor_main(doc):
    menu(doc)
    while True:
        asked_func = ' '
        while True:
            asked_func = input()
            if(asked_func not in ['1', '2', '3', '4', '5', '6', '7', '8']):
                print("Wrong input")
            else:
                break

        if not DOCTOR_OPTIONS[int(asked_func)](doc):
            break

    return True


if __name__ == '__main__':
    doctor_main(Doctor("Dr. Albena Bachvarova", 1))
