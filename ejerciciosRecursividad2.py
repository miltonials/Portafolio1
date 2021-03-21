"""
•Nombre: corrimientoAEntero
•Entradas: num
•Salidas: la entrada pero con los decimales corridos a la parte entera.
•Restricciones: la entrada debe ser un número flotante positivo.
"""


def corrimientoAEntero(num):
    if (isinstance(num, float) and num > 0):
        return int(corrimientoAEntero_aux(num, 0))
    else:
        print("Error: el dígito que ingresaste debe ser entero mayor a 0")


def corrimientoAEntero_aux(num, potencia):
    if((num * 10 ** potencia) % 1 == 0):  # Si residuo es 0 entonces no hay más decimales
        return potencia
    elif(potencia == 0):
        return num * (10 ** corrimientoAEntero_aux(num, potencia + 1))
    else:
        return corrimientoAEntero_aux(num, potencia + 1)


"""
•Nombre: contarDigitos
•Entradas: num
•Salidas: cantidad de dígitos de la entrada (inclyendo decimales).
•Restricciones: la entrada debe ser un número del conjunto de los número reales

Nota: se hará uso de corrimientoAEntero_aux para contar los números flotantes
"""


def contarDigitos(num):
    if (isinstance(num, float) or isinstance(num, int)):
        num = convertir_a_positivo(num)
        if (isinstance(num, float)):
            num = int(corrimientoAEntero_aux(num, 0))
            return contarDigitos_aux(num)
        else:
            return contarDigitos_aux(num)
    else:
        print("Error: debes ingresar únicamente números")


def convertir_a_positivo(num):
    if num < 0:
        return -num
    else:
        return num


def contarDigitos_aux(num):
    if num == 0:
        return 0
    else:
        return 1 + contarDigitos_aux(num // 10)
