'''
Enunciado: Convierte un Excel a CSV

Objetivo:

Aprender a trabajar con ficheros

Usar la librería pandas de Python
'''

import pandas as pd

ruta_excel = 'ruta/archivo/excel.xlsx'
ruta_csv = 'ruta/archivo/file.csv'


datos_excel = pd.read_excel(ruta_excel)

datos_excel.to_csv(ruta_csv, index=False)


