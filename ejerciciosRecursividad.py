"""
•Nombre: divisores
•Entrada: num (un número entero positivo)
•Salida: divisores de num de manera descendente
•Restricción: la entrada debe ser un numero entero positivo
"""


def divisores(num):
    if(isinstance(num, int)):
        print(num, " es divisible entre:")
        return divisores_aux(num, num)
    else:
        print("Debes digitar un número entero")
        return -1


def divisores_aux(num, divisor):
    if (divisor == 1):
        return 1
    elif(num % divisor == 0):
        print(divisor)
    return divisores_aux(num, divisor - 1)

"""
•Nombre: multiplicarRecusivo
•Entrada: num, factor ( ambos números enteros)
•Salida: multiplicación de num por el factor sin utilizar el operador de multiplicacioón
•Restricciones: las entradas deben ser número enteros
"""
def multiplicarRecusivo(num, factor):
    if(isinstance(num, int) and isinstance(factor, int)):
        if(factor == 0):
            return 0
        elif(factor < 0):
            return -num + multiplicarRecusivo(num, factor + 1)
        else:
            return num + multiplicarRecusivo(num, factor - 1)
    else:
        print("Error: debes digitar un número entero")
