from queries import *
# from menu import *
from prettytable import PrettyTable


class Doctor():
	def __init__(self, username, id_):
		self.name = username
		self.id = id_
		self.options = {
			3: self.list_patients
		}

		self.main()

	def menu(self):
		options = '''
Welcome {0}, you are logged in as Doctor!
1 Register
2 Log into the system
3 List all patients
4 Add hour for visitation
5 Delete free hours of visitation
6 Log out
'''.format(self.name)
		return options

	def list_patients(self):
		patients = c.execute(SLECT_DOCTOR_PATIENTS, self.id)
		patient_table = PrettyTable()
		patient_table.field_names = ["Patients"]
		for patient in patients:
		   patient_table.add_row = ([patient['USERNAME']])
		print(list_patients)


	def main(self):
		print(self.menu())
		while(1):
			func_call = input()
			self.options[int(func_call)]()
