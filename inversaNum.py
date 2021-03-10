def contarDigitos(num):
    if (isinstance(num, int)) == False:
        return print("Error: tipo de dato no es entero")
    elif(num == 0):
        return 1
    else:
        return contarDigitos_aux(num)


def contarDigitos_aux(num):
    if num == 0:
        return 0
    else:
        return 1 + contarDigitos_aux(num // 10)


"""
•Nombre: reversaNumero
•Entrada:num (será un número entero mayor o igual a 0)
•Salida: numero entero mayor a 0 con orden inverso a la entrada
•Restricción: entero positivo mayor o igual a 0
"""


def reversaNum(num):
    if (isinstance(num, int)):
        if num >= 0:
            if num <= 0:
                return num
            else:
                return reversaNum_aux(num, contarDigitos(num))
        else:
            print("El número debe de ser positivo")
    else:
        print("Error: el número debe de ser entero")


def reversaNum_aux(num, largo_num):
    if (largo_num == 0):
        return 0
    else:
        return (num % 10) * (10 ** (largo_num - 1)) + reversaNum_aux(num // 10, largo_num - 1)