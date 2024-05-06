from PIL import Image
import numpy as np

def desencriptador_imagen(imagen)->list:
    secuencia = []
    matriz_imagen = np.array(imagen)
    alto_imagen = len(matriz_imagen)
    ancho_imagen = len(matriz_imagen[0])
    for i in range(0, alto_imagen, 2):
        for j in range(0, ancho_imagen, 2):
            seccion = matriz_imagen[i: i+2, j: j+2]
            varianza = np.var(seccion, axis=(0, 1))
            var_minima = np.argmin(varianza)
            promedio = np.mean(seccion[:,:,var_minima], axis=(0, 1))
            verdadero_valor = (seccion[1, 1, var_minima] - promedio) 
            if verdadero_valor < -1:
                verdadero_valor + 256
            secuencia.append(verdadero_valor)
            if verdadero_valor == 0:
                break
            else:
                continue
    return secuencia

def desencrpitar_mensaje(secuencia)->str:
    #Le resto a la toda la secuencia 1, excepto a los -1's  y al 0
    for i in range(len(secuencia)):
        if secuencia[i] != -1 or secuencia[i] != 0:
            secuencia[i] = secuencia[i] -1
        elif secuencia[i] == 0:
            break

    #Junto los digitos que esten entre -1's
    mensaje = ""
    nueva_secuencia = []
    for numero in secuencia:
        if numero == -1:
            nueva_secuencia.append(int(mensaje))
            mensaje = ""
            nueva_secuencia.append(numero)
        elif numero == 0:
            break
        else:
            mensaje += str(numero)

    #Convierto en letras y caracteres la secuencia de numeros
    tabla_numeros_caracteres = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' ', 28: '.',
    29: ',', 30: '?', 31: '!', 32: '¿', 33: '¡', 34: '(', 35: ')', 36: ':', 37: ';',
    38: '-', 39: '“', 40: '‘', 41: 'á', 42: 'é', 43: 'í', 44: 'ó', 45: 'ú', 46: 'ü',
    47: 'ñ'
    }
    mensaje = []
    for numero in nueva_secuencia:
        if numero == 0:
            break
        elif numero == -1:
            continue
        else:
            caracter = (tabla_numeros_caracteres[numero])
            mensaje.append(caracter)
    return mensaje


imagen = np.array(Image.open('encrypted_baboon.png'))
secuencia = desencriptador_imagen(imagen)
print(desencrpitar_mensaje(secuencia))

        
