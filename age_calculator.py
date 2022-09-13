# This program will check if the date is valid
# and it will calculate the age of the person.
# Practising manipulating dates in Python.
# Author: Marcelo Magario - 04/09/2022

import datetime

input_date = input('Enter your date of birthday (dd/mm/yyyy): ')


def check_date(input_date)
frase = ''
day, month, year = input_date.split('/')
valid_date = True
try:
    datetime.datetime(int(year), int(month), int(day))
except ValueError:
    valid_date = False
    # if valid_date:
    #     frase = 'The date is valid.'
    # else:
    #     frase = 'Date is invalid, please try again.'

check_date(input_date)
print(frase)


# today_is = datetime.datetime.now() # receive today's date
# print(today_is)
# print(f'Today is: {today_is.strftime("%A")} - {today_is.day}/{today_is.month}/{today_is.year}')
# # x = datetime.datetime(2020, 5, 31)

