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

"""
•Nombre: indiceNumero
•Entradas: num, indice
•Salidas: el dígito del número, según el índice que se introdujo
•Restricciones las entradas deben ser números enteros positivos

Nota: se utiliza contarDigitos_aux para verificar que el índice no sobrepase la cantidad de dígitos del número ingresado.
"""

def indiceNumero(num, indice):
    if(isinstance(num, int) and isinstance(indice,int)):
        if(num > 0 and indice >= 0):
            return indiceNumero_aux(num, indice)
        else:
            print("Error: debes digitar solamente números positivos")
    else:
        print("Error: solamente puedes introducir  números enteros positivos")

def indiceNumero_aux(num, indice):
    cantidad_de_digitos = contarDigitos_aux(num)
    num = inversa_de(num, contarDigitos_aux(num))
    if(cantidad_de_digitos - 1 < indice):
        print("Digitaste un indice mayor a la cantidad de dígitos que ingresaste.")
        print("Recuerda que empezamos a contar desde el índice 0.")
    elif(indice == 0):
        return num % 10
    else:
        return (num // 10**indice) % 10

def inversa_de(num, largo_num):
    if (largo_num == 0):
        return 0
    else:
        return (num % 10) * (10 ** (largo_num - 1)) + inversa_de(num // 10, largo_num - 1)

"""
•Nombre: cortarNumero
•Entradas: num, indice1, indice2
•Salidas: Un nuevo número según el índice 
•Restricciones:  en las entradas num debe ser mayor a 0 y ambos indices deben ser mayores o iguales a 0.

Nota: se utiliza indiceNumero_aux para obtener mediante la recursividad los dos nuevos números según los índice que se introdujeron.
"""

def cortarNumero(num, indice1, indice2):
    if(isinstance(num, int) and isinstance(indice1,int) and isinstance(indice2, int)):
        if(num > 0 and indice1 >= 0 and indice2 >= 0):
            return cortarNumero_aux(num, indice1, indice2)
        else:
            print("Error: debes digitar solamente números positivos")
    else:
        print("Error: solamente puedes introducir  números enteros positivos")

def cortarNumero_aux(num, indice1, indice2):
    nuevoNumero1 =  indiceNumero_aux(num, indice1)
    nuevoNumero2 = indiceNumero_aux(num, indice2)
    if (isinstance(nuevoNumero1, int) and isinstance(nuevoNumero2, int)):
        return (nuevoNumero1) + (nuevoNumero2*10)
