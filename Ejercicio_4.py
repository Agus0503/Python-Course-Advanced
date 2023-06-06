'''
Enunciado: Utilizando la API de https://openweathermap.org/ y realizando
una petición a https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={API%20key},
obtén la temperatura máxima y mínima, para la ciudad que proporcione el usuario.

Objetivo:

Aprender a utilizar librerías externas (en este caso, requests)

Manipular el resultado de la petición (JSON)
'''

import requests

api_key = "CLAVE_API"  
city_name = input("Ingrese nombre de la ciudad: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]
    print(f"Temperatura máxima: {temp_max}°C")
    print(f"Temperatura mínima: {temp_min}°C")
else:
    print("Error en la solicitud:", response.status_code)
