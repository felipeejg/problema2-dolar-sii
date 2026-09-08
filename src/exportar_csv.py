import numpy as np
import csv
from cargar_datos import cargar_dolar_sii
from errores import redondeo_vec, calcular_error_absoluto_relativo

def generar_csv_errores():
    #cargar datos(12 meses x 4 años)
    datos = cargar_dolar_sii()
    años = [2022, 2023, 2024, 2025]
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    
    nombre_archivo = 'tabla_errores_evaluados.csv'
    
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        #encabezados requeridos por la rúbrica
        writer.writerow(['Anio', 'Operacion', 'Valor_Real', 'Valor_Aprox', 'Error_Absoluto', 'Error_Relativo(%)', 'Error_Propagado_Absoluto'])
        
        for j, año in enumerate(años):
            #error de representación mensual (con 3 cifras significativas para variar)
            for i, mes in enumerate(meses):
                real = datos[i, j]
                aprox = redondeo_vec(real, 3) 
                ea, er = calcular_error_absoluto_relativo(real, aprox)
                #como es solo representación, no hay error propagado aún
                writer.writerow([año, f'Representacion_{mes}', real, aprox, round(ea, 4), round(er, 4), '-'])
                
            #evaluación entre dos puntos (Variación Anual Enero a Diciembre)
            enero_real = datos[0, j]
            dic_real = datos[11, j]
            
            enero_aprox = redondeo_vec(enero_real, 3)
            dic_aprox = redondeo_vec(dic_real, 3)
            
            ea_enero, _ = calcular_error_absoluto_relativo(enero_real, enero_aprox)
            ea_dic, _ = calcular_error_absoluto_relativo(dic_real, dic_aprox)
            
            #resta real y aproximada
            var_real = dic_real - enero_real
            var_aprox = dic_aprox - enero_aprox
            
            #en la resta, el error absoluto se propaga sumando los errores absolutos individuales
            error_prop_abs = ea_enero + ea_dic
            
            #error real de la operación de variación
            ea_var, er_var = calcular_error_absoluto_relativo(var_real, var_aprox)
            
            writer.writerow([año, 'Variacion_Ene_Dic', round(var_real, 2), round(var_aprox, 2), round(ea_var, 4), round(er_var, 4), round(error_prop_abs, 4)])

if __name__ == "__main__":
    generar_csv_errores()