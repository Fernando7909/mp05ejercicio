# Ejercicio 1

def validar_parentesis(expressio):
    pila = []
    for car in expressio:
        if car == '(':
            pila.append(car)  # Afegim un parèntesi obert
        elif car == ')':
            if len(pila) == 0:
                return False  # Parèntesi de tancament sense obertura
            pila.pop()  # Eliminem un parèntesi obert
    return len(pila) == 0  # Si la pila està buida, els parèntesis estan equilibrats


# Prova de l'exemple
expressio = "(a + b) * (c + d)"
print(validar_parentesis(expressio))  # True

expressio = "(a + b * (c - d)"
print(validar_parentesis(expressio))  # False



# Ejercicio 2

def invertir_cadena(cadena):
    pila = []
    # Afegir cada caràcter a la pila
    for car in cadena:
        pila.append(car)

    cadena_invertida = ""
    # Treure els caràcters de la pila per invertir
    while len(pila) > 0:
        cadena_invertida += pila.pop()
    return cadena_invertida


# Prova de l'exemple
cadena = "Python"
print(invertir_cadena(cadena))  # "nohtyP"

