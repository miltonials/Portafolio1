"""
•Nombre: corrimientoAEntero
•Entradas: num
•Salidas: la entrada pero con los decimales corridos a la parte entera.
•Restricciones: La entrada debe ser un número flotante positivo.
"""


def corrimientoAEntero(num):
    if (isinstance(num, float) and num > 0):
        return int(corrimientoAEntero_aux(num, 0))
    else:
        print("Error: edl dígito que ingresaste debe ser entero mayor a 0")


def corrimientoAEntero_aux(num, potencia):
        if((num * 10 ** potencia) % 1 == 0): #Si residuo es 0 entonces no
            return potencia
        elif(potencia == 0):
            return num * (10 ** corrimientoAEntero_aux(num, potencia + 1))
        else:
            return corrimientoAEntero_aux(num, potencia + 1)