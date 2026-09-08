import numpy as np
from cargar_datos import cargar_dolar_sii
from errores import redondeo_vec, calcular_error_absoluto_relativo

def calcular_variacion_anual():
    datos = cargar_dolar_sii()
    #enero (fila 0) y diciembre (fila 11)
    enero = datos[0, :]
    diciembre = datos[11, :]
    
    #redondeamos simulando punto flotante de baja precisión (3 cifras como pide A3/A4)
    enero_aprox = redondeo_vec(enero, 3)
    diciembre_aprox = redondeo_vec(diciembre, 3)
    
    #calculamos errores absolutos iniciales
    ea_enero, _ = calcular_error_absoluto_relativo(enero, enero_aprox)
    ea_diciembre, _ = calcular_error_absoluto_relativo(diciembre, diciembre_aprox)
    
    #resta real y aproximada
    variacion_real = diciembre - enero
    variacion_aprox = diciembre_aprox - enero_aprox
    
    #propagación: en la resta los errores absolutos se suman
    error_propagado_abs = ea_enero + ea_diciembre
    
    #calcular el error porcentual respecto a la variación real
    #abs() para evitar porcentajes negativos
    error_porcentual = (error_propagado_abs / np.abs(variacion_real)) * 100
    
    #guardamos los resultados en una lista para poder ordenarlos
    resultados = []
    años = [2022, 2023, 2024, 2025]
    
    for i, año in enumerate(años):
        resultados.append({
            'año': año,
            'variacion': variacion_aprox[i],
            'error_abs': error_propagado_abs[i],
            'error_porc': error_porcentual[i]
        })
        
    #ordenar de más confiable (menor error porcentual) a menos confiable
    resultados_ordenados = sorted(resultados, key=lambda x: x['error_porc'])
    
    print("Variación Anual (Ordenada por confiabilidad):")
    print("-" * 50)
    for res in resultados_ordenados:
        print(f"Año {res['año']}: Variación aprox {res['variacion']:.2f} +/- {res['error_abs']:.2f} CLP "
              f"| Error Porcentual: {res['error_porc']:.2f}%")

if __name__ == "__main__":
    calcular_variacion_anual()