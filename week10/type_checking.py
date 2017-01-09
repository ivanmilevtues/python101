import sys
import re


def check_name(func_name):
	if re.search("\W+", func_name):
		return False

	if not func_name.islower():
		return False
	return True


def validate(func_def):
	func_def = func_def[:-1]
	func_elements = func_def.split(' ')

	if not check_name(func_elements[0]):
		return False

	for el in func_elements:
		if el != '::' and el != '->' and el != '.':
			if re.search("\W+|\[\]", el):
				print(el)
				return False
	return True


def validate_file(inpt):
	for element in inpt:
		if element != '\n':
			if not validate(element):
				return False
	return True


def parse_input(inpt):
	result = {}
	try:
		for func in inpt:
			if validate(func):
				splitted = func.split(' :: ')
				key = splitted[0]
				values = splitted[1].split(' -> ')
				values[len(values) - 1] = values[len(values) - 1][:-1]
				result[key] = values
	except IndexError:
		return result


def check_type_rule(inpt):
	for el in inpt:
		if '.' in el:
			functions = el.split(' . ')
			if functions[-1][-1] == '\n':
				functions[-1] = functions[-1][:-1]

	functions = functions[::-1]
	# print("functions =>", end="")
	# print(functions)
	data_flow = []
	func_args = parse_input(inpt)
	for func_name in functions:
		for i in func_args[func_name]:
			data_flow.append(i)
	data_flow = data_flow[1:len(data_flow) - 1]
	for i in range(len(data_flow)):
		if i % 2 == 0:
			if data_flow[i] != data_flow[i + 1]:
				return False
	return True


def main():
	inpt = list(sys.stdin)
	if not validate_file(inpt):
		print("False")
		return 0
	print(check_type_rule(inpt))

if __name__ == '__main__':
	main()
