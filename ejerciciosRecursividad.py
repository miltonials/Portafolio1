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
