import math

#Funciones normales
def potencia(x):
    return x**2
print(potencia(3))


def area_cilindro(r,h):
    return math.pi * r**2 * h
print(area_cilindro(2,5))


#Funciones lambda
a_cilindro = lambda r,h: math.pi * r**2 * h
print(a_cilindro(2,5))


#Funcion recursiva(se llama a si misma)
"""Factorial: 3! = 3*2*1"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))