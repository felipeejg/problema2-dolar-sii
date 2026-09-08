import numpy as np

def cargar_dolar_sii(ruta_archivo='data/dolar_observado_sii_2022_2025.csv'):
    #extraemos solo la columna de valores numéricos, separador punto y coma
    valores = np.genfromtxt(ruta_archivo, delimiter=';', skip_header=1, usecols=(3))
    
    #el archivo tiene 48 datos (12 meses x 4 años).
    #lo redimensionamos a (4, 12) y luego lo transponemos (.T) para que quede de (12, 4)
    #así la fila 0 será Enero de todos los años, y la fila 11 Diciembre.
    matriz_dolar = valores.reshape(4, 12).T
    return matriz_dolar

if __name__ == "__main__":
    matriz_dolar = cargar_dolar_sii()