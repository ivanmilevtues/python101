from user_func import *
from doctor_func import *
from patient_func import *

CALL_BASIC_FUNC = {
	1: login,
	2: register,
	3: start_options,
	4: exit
}


def control_block():
	start_options()
	user = None
	while True:
		asked_func = ' '
		while True :
			asked_func = input()
			if(asked_func not in ['1', '2', '3', '4']):
				print("Wrong input")
			else:
				break
		user = CALL_BASIC_FUNC[int(asked_func)]()
		if not user:
			break
		if type(user) is Patient:
			patient_main(user)
		if type(user) is Doctor:
			doctor_main(user)

def main():
	control_block()

if __name__ == '__main__':
	main()
