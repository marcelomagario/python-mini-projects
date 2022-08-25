# Program where the user enter the number of Fibonacci elements to show in the list.

n = int(input('Digite a quantidade de elementos Fibonacci: '))
fibo = [1, 1]
penultimo = 1
ultimo = 1

for i in range(2, n):
    soma = ultimo + penultimo
    fibo.append(soma)
    penultimo = ultimo
    ultimo = soma
print(fibo)

