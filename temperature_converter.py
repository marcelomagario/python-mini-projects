# convert fahrenheit to celsius
fah = float(input('What is the Fahrenheit temperature you want to convert? '))

def transformar_para_celsius():
    celsius = 5 * ((fah - 32)/9)
    print(f'This temperature in Celsius is  {celsius:.0f} C')

transformar_para_celsius()

