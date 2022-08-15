n = int(input('Choose a number between 1 and 10: '))
if 0 < n <= 10:
    for i in range(1, 11):
        print(f'{n} X {i} = {n * i}')
else:
    print('Choose number between 1 and 10')


# def multiplication_table(n: int) -> str:
#     if 0 < n <= 10:
#         for i in range(1, 11):
#
#             return f'{n} X {i} = {n * i}'
#     else:
#         return 'Choose number between 1 and 10'
