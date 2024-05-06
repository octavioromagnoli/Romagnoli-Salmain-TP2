from PIL import Image
import numpy as np

def encriptador(mensaje)->list: 
    mensaje = mensaje.lower()
    tabla_caracteres_numeros = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '.': 28,
        ',': 29, '?': 30, '!': 31, '¿': 32, '¡': 33, '(': 34, ')': 35, ':': 36, ';': 37,
        '-': 38, '“': 39, '‘': 40, 'á': 41, 'é': 42, 'í': 43, 'ó': 44, 'ú': 45, 'ü': 46,
        'ñ': 47
    }
    secuencia = []
    for caracter in mensaje:
        numero = str(tabla_caracteres_numeros[caracter])
        for digito in numero:
            secuencia.append(int(digito) + 1)
        secuencia.append(-1)
    secuencia.append(0)
    return secuencia
    
def mensaje_en_imagen(secuencia,imagen)->list[list[list]]:
    alto_imagen = len(imagen)
    ancho_imagen = len(imagen[0])
    numero = 0
    for i in range(0, alto_imagen-1, 2):
        for j in range(0, ancho_imagen-1, 2):
            seccion = imagen[i: i+1, j: j+1]
            varianza = np.var(seccion, axis=(0, 1))
            var_minima = np.argmin(varianza)
            promedio = np.mean(seccion[:,:,var_minima], axis=(0, 1))
            nuevo_valor = (promedio + secuencia[numero]) %256
            imagen[i+1][j+1][var_minima] = nuevo_valor
            if secuencia[numero] == 0:
                break
            numero += 1
    return imagen

    
mensaje = 'Hola, como estas todos?'
secuencia = encriptador(mensaje)
imagen = np.array(Image.open('kuwahara_baboon.png'))
mensaje_encriptado = mensaje_en_imagen(secuencia, imagen)
print(secuencia)
print(mensaje_encriptado)