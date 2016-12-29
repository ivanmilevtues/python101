import sqlite3

from queries import *
from user_func import *
from user import Patient
from prettytable import PrettyTable


def menu(usr):
	print("""
1. Register
2. Log into the system
3. Reserve hour for visitation
4. Stay at the hospital for an injury
5. See the academic title of his doctor
6. Logout
7. Exit
""")
	return True


def reserve_visit_hour(usr):
	print("Reserve visit hours:")
	doctor = input("The name of your doctor: ")
	start_hour = input("The start hour of the visitation: ")
	docotors = c.execute(SELECT_PATIENT_DOCTOR, [usr.get_id(), ])

	for doc in docotors:
		print("Searching for doctor...")
		if doc['USERNAME'] == doctor:
			print("Patient found. Adding visitation...")
			c.execute(INSERT_VISITATION_HOUR, [usr.get_id(),
					  doc['id'], start_hour, ])
			print("Visitation added.")

	db.commit()
	return True


def make_hospital_reservation(usr):
	print("Make hospital stay reservation:")
	start_date = input("Start Date: ")
	end_date = input("End Date: ")
	room = input("Room Number: ")
	injury = input("Injury: ")
	print("Adding hospital stay...")
	c.execute(INSERT_INTO_HOSPITAL_STAY, [start_date, end_date, room,
										  injury, usr.get_id(), ])
	print("Hospital stay added.")
	db.commit()
	return True


def take_doc_acad_title(usr):
	doctors = c.execute(SELECT_PATIENT_DOCTOR, [usr.get_id(), ])
	
	for doc in doctors:
		titles = c.execute(SELECT_DOCTOR_TITLE, [doc['id'], ])
		for title in titles:
			print("{0}'s' title: {1}".format(doc['USERNAME'] ,title['ACADEMIC_TITLE']))
	return True


PATIENT_OPTIONS = {
	1: register,
	2: login,
	3: reserve_visit_hour,
	4: make_hospital_reservation,
	5: take_doc_acad_title,
	6: logout,
	7: exit
}


def patient_main(pat):
	menu(pat)
	while True:
		asked_func = ' '
		while True:
			asked_func = input()
			if(asked_func not in ['1', '2', '3', '4', '5', '6', '7']):
				print("Wrong input")
			else:
				break

		if not PATIENT_OPTIONS[int(asked_func)](pat):
			break

	return True

if __name__ == '__main__':
	patient_main(Patient("Kristina Valchanova", 2))
