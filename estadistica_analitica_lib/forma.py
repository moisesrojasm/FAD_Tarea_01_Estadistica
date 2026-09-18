# Momento central, 
# coeficiente Fisher-Pearson momentos
# coeficiente asimetría Pearson 1
# coeficiente asimetría Pearson 2
# coeficiente de sesgo cuantiles
# exceso curtosis 
# curtosis percentílica 

def momento_central(r, datos_frecuencias, datos_tendencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    media = datos_tendencias["Media Aritmetica"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma += fi[i] * ((xi[i] - media) ** r)

    return suma / N

