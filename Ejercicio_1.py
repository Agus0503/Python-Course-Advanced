'''
Enunciado: Imprime todos los ficheros existentes en tu carpeta de Descargas.

Objetivo:
Aprender a utilizar librerías sencillas (en este caso, os) y sus funciones.
Aprender a utilizar los bucles y los condicionales.

El algoritmo del ejercicio es el siguiente:
Obtén todos los ficheros y directorios de un directorio en concreto.
Para ello necesitas una función existente en la librería os (Sistema Operativo) de Python.
Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.

Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os.

Ampliación:
Lista los tamaños de los ficheros en formato humano.
Recorre de manera recursiva todos los directorios desde tu carpeta personal y muestra los ficheros de cada directorio y su tamaño
'''

import os

def lista_ficheros(directorio):
    for fichero in os.listdir(directorio):
        if os.path.isfile(os.path.join(directorio, fichero)):
            print(f"Fichero: {fichero}")
            print(f"Tamaño del fichero {fichero}:",os.path.getsize(os.path.join(directorio, fichero)))
            
#lista_ficheros('directorio')

