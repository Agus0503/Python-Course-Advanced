'''
Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
Añadir a cualquier persona, indicando nombre y después teléfono
Buscar el teléfono de una persona

Objetivo:
Aprender a manejar la entrada y la salida por consola.
El uso de colecciones (array o diccionario)

Ampliación:
Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
Introduce un nombre: Pep
Resultados:

Pepe 659331013
Pepe Martín 633743551

'''

from os import system

def menu():
    print("Bienvenido a la agenda de teléfonos")
    print("1. Añadir a cualquier persona")
    print("2. Buscar el teléfono de una persona")
    print("3. Salir")


def agregar(lista:list):
    system('clear')
    nombre = input("Ingrese el nombre de la persona: ")
    telefono = input("Ingrese el teléfono de la persona: ")
    lista.append([nombre, telefono])
    return lista

def buscar(lista: list):
    system('clear')
    nombre = input("Ingrese el nombre de la persona que desea buscar: ")
    
    if len(lista) > 0:
        resultados = []
        for i in range(len(lista)):
            if nombre.lower() in lista[i][0].lower():
                resultados.append(lista[i])
        
        if len(resultados) > 0:
            print("Resultados:")
            for resultado in resultados:
                print(f"{resultado[0]} {resultado[1]}")
        else:
            print("No existen nombres coincidentes en la agenda")
    else:
        print("La agenda está vacía")

def validar_entero(numero_str):
    """_summary_
        Valido que la cadena recibida contenga o no un numero entero
    Args:
        numero_str (str): cadena a evaluar
    Returns:
        bool: True si la cadena contiene un numero entero
              False si la cadena no contiene un numero entero  
    """    
    retorno = False

    if len(numero_str):
        if numero_str.isnumeric() or (numero_str[0] == "-" and numero_str[1:].isnumeric()):
            retorno = True
            
    return retorno


agenda = []

while True:
    
    menu()
    opcion = input("Elija una opción: ").strip()

    if validar_entero(opcion):
        opcion = int(opcion)
        while opcion < 1 or opcion > 3:
            system('clear')
            menu()
            opcion = input("Error, opción incorrecta | Elija una opción: ").strip()
            if validar_entero(opcion):
                opcion = int(opcion)
    
    match opcion:
        case 1:
            agenda = agregar(agenda)
        case 2:
            buscar(agenda)
        case 3:
            print("Programa Finalizado")
            break
        
    input("Presione enter para continuar...")
    system('clear')