'''
Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.

Objetivo:

Uso de bucles anidados

El uso de colecciones
'''


def primos(n):
    primos = []
    for i in range(1, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primos.append(i)
    return primos

numeros_primos = primos(17)
print(numeros_primos)