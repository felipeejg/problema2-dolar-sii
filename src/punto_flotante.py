import numpy as np

def comprobar_cancelacion():
    #precios de Diciembre 2022 y 2023
    p_dic22 = 875.66
    p_dic23 = 874.67
    
    #forzando precisión simple (32 bits)
    diff_32 = np.float32(p_dic23) - np.float32(p_dic22)
    
    #forzando precisión doble (64 bits)
    diff_64 = np.float64(p_dic23) - np.float64(p_dic22)
    
    print(f"Resultado en Float32 (~7 cifras): {diff_32}")
    print(f"Resultado en Float64 (~15 cifras): {diff_64}")

if __name__ == "__main__":
    comprobar_cancelacion()