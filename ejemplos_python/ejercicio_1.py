"""Imprime por consola todos los números pares desde el 1 hasta el 100 utilizando un bucle for"""

i = 100
for i in range(1,101):
    if i%2 == 0:
        print(i)

for i in range(2,101,2):
    print(i)