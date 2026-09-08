import numpy as np

def aplicar_cifras_significativas(x, cifras=2):
    if x == 0:
        return 0.0
    return np.round(x, cifras - int(np.floor(np.log10(np.abs(x)))) - 1)

#vectorizamos para aplicar a matrices completas sin usar bucles
redondeo_vec = np.vectorize(aplicar_cifras_significativas)

def calcular_error_absoluto_relativo(real, aprox):
    ea = np.abs(real - aprox)
    er = (ea / real) * 100
    return ea, er