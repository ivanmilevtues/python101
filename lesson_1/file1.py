# 2016-10-17 First programming lesson in HackBulgaria
# For loop | While | If statement | function
# pep8 convention!

# list_of_numbers = input("Enter your first name: ")
# for char in list_of_numbers:
#     print(char)

list_of_numbers = [1, 3, 8, 9, 10, 190, 209]

print(list_of_numbers)
for indx in range(len(list_of_numbers)):
    list_of_numbers[indx] **= 2



def function_1(list_of_numbers):
    for el in list_of_numbers:
        if el % 2 == 0:
            print(el)
    return list_of_numbers

print(function_1(list_of_numbers))
