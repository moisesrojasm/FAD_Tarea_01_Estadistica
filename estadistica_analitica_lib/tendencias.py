# Promedio: aritmético, geométrico, armónico
# Mediana, moda y RCM
# Cuantiles: cuartiles, deciles y percentiles

import math

def media_aritmetica(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma += (fi[i] * xi[i])

    return suma / N

def media_geometrica(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):    
        suma += (fi ** math.log10(xi))

    return 10 ** (suma / N)

def media_armonica(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma += (fi / xi)

    return N / suma

#def mediana(datos_frecuencias):

#def moda(datos_frecuencias):

def rcm(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma *= (fi * xi ** 2)

    return math.sqrt(suma / N)

#def cuantil(datos_frecuencia, k, q):
