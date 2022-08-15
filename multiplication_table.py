def multiplication_table(n: int) -> str:
    if 0 < n <= 10:
        for i in range(1, 11):

            return f'{n} X {i} = {n * i}'
    else:
        return 'Choose number between 1 and 10'

