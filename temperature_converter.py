# convert fahrenheit to celsius
# Author Marcelo Magario
fah = float(input('What is the Fahrenheit temperature you want to convert? '))


def transformar_para_celsius():
    celsius = 5 * ((fah - 32)/9)
    print(f'This temperature in Celsius is  {celsius:.0f} C')


transformar_para_celsius()

celsius = float(input('What is the Celsius temperature you want to convert? '))


def transformar_para_fahrenheit():
    farenheit = 32 + ((9 * celsius)/5)
    print(f'This temperature in Fahrenreit is {farenheit:.0f} F')


transformar_para_fahrenheit()
