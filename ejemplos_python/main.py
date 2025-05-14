print("Hola Mundo")

# Variables
saludo = "Maquina"
print("Hola " + saludo)

# Condicionales
if 1>2:
    print("Es verdad")
else:
    print("Es mentira")

print(3+2)
print(3**3)
print(19%2)


print("introduce un numero para saber si es un numero primo: ")
numero_intro = int(input())

num = numero_intro - 1
primo = true

while primo and num > 1:
    resultado = numero_intro % num
    print(resultado)
    num -= 1
    if resultado == 0:
        primo == False

if primo == True:
    print("Es primo")
else:
    print("no es primo")