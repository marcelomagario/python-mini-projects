# program to check if the number entered is a prime number

n = int(input('Enter the number you want to verify is is Prime: '))
result = ''
if n < 2:
    result = 'It is not Prime'
elif n ==2:
    result = 'It is Prime'
for i in range(2, n):
    if (n % i) == 0:
        print('It is NOT Prime')
        break
    else:
        print('It is Prime')
        break

