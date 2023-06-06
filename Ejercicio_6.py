'''
Enunciado: Crea una función que convierta un password (entre 6 y 12 caracteres) es una 
cadena de texto alfanumérica de 32 caracteres.
La función SIEMPRE debe devolver el mismo resultado para la misma entrada.

Objetivo:

Aprender a manejar los bucles y las cadena de texto.

Mejorar la capacidad algorítmica.
'''

import random
import string

def convertir_password(password):
    
    if len(password) > 6 and len(password) < 12:
        caracteres_faltantes = 32 - len(password)
        caracteres_aleatorios = ''.join(random.choices(string.ascii_letters + string.digits, k=caracteres_faltantes))
        password += caracteres_aleatorios
    
    return password


new_password = convertir_password("password")
print(new_password)