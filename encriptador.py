from PIL import Image
import numpy as np
from desencriptador import desencrpitar_mensaje
from funciones2 import lesser_variance, todos_menos_infd, get_shape


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
    alto_imagen, ancho_imagen, _ = get_shape(imagen)
    numero = 0
    
    for i in range(0, alto_imagen-1, 2):
        for j in range(0, ancho_imagen-1, 2):
            seccion = imagen[i: i+2, j: j+2]

            sin_inf_der = todos_menos_infd(seccion)

            var_minima, color_sin_infd = lesser_variance(sin_inf_der)
            
            promedio = np.floor(np.mean(color_sin_infd))

            nuevo_valor = (promedio + secuencia[numero]) %256
            imagen[i+1,j+1,var_minima] = nuevo_valor
            if secuencia[numero] == 0:
                break
            numero += 1
    return imagen

mensaje = 'salio todo bien bien ahi genial'
secuencia = encriptador(mensaje)
imagen = np.array(Image.open('kuwahara_baboon.png'))
mensaje_encriptado = mensaje_en_imagen(secuencia, imagen)
print(secuencia)
print(mensaje_encriptado)
imagen = Image.fromarray(mensaje_encriptado.astype('uint8'))
imagen.save('prueba_baboonx.png')
