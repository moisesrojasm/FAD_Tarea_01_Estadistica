# Momento central, 
# coeficiente Fisher-Pearson momentos
# coeficiente asimetría Pearson 1
# coeficiente asimetría Pearson 2
# coeficiente de sesgo cuantiles
# exceso curtosis 
# curtosis percentílica 

import math

def momento_central(r, datos_frecuencias, datos_tendencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    media = datos_tendencias["Media Aritmetica"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma += fi[i] * ((xi[i] - media) ** r)

    return suma / N

def coef_fp_momentos(datos_frecuencias, datos_tendencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    media = datos_tendencias["Media Aritmetica"]
    N = datos_frecuencias["N"]

    suma1 = suma2 = 0
    for i in range(len(fi)):
        suma1 += (fi[i] * (xi[i] - media) ** 3) / N
        suma2 += (fi[i] * (xi[i] - media) ** 2) / N

    return suma1 / suma2 ** (3/2)

def coef_asim_p1(datos_tendencias, datos_dispersion):
    media = datos_tendencias["Media Aritmetica"]
    moda = datos_tendencias["Moda"]
    varianza = datos_dispersion["Varianza"]

    return (media - moda) / varianza

