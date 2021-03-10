"""
•Nombre: contarPares
•Entrada:num (será un número entero mayor o igual a 0)
•Salida: cantidad de dígitos pares de la entrada
•Restricción: entero positivo mayor a 0
"""
def contarPares(num):
    if(isinstance(num, int) and num > 0):
        return contarParesAux(num)


def contarParesAux(num):
    if num == 0:
        return 0
    elif(num % 2 == 0):
        return 1 + contarParAux(num // 10)
    else:
        return 0 + contarParAux(num // 10)
