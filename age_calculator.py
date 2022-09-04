# This program will check if the date is valid
# and it will calculate the age of the person.
# Practising manipulating dates in Python.
# Author: Marcelo Magario - 04/09/2022

import datetime

today_is = datetime.datetime.now() # receive today's date
print(today_is)
print(f'Today is: {today_is.strftime("%A")} - {today_is.day}/{today_is.month}/{today_is.year}')
# x = datetime.datetime(2020, 5, 31)
#dob = date
