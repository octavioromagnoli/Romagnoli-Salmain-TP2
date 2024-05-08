from PIL import Image
import numpy as np

def get_shape(array: list)->tuple[int, int, int]:
    '''
    Toma un array y devuelve una tupla con los largos de cada dimension
    Argumentos:
        array : np.array
            El array del que se quiere saber la forma
    '''
    return array.shape

def prom_menos_infd(array: list)->list:
    lista = []
    for i in range(2):
        for j in range(2):
                lista.append(array[i, j])
    lista[3] = 0
    suma = 0
    for i in lista:
        suma += i
    promedio = suma/3
    return np.floor(promedio)

def todos_menos_infd(array:list)->list:
    imagen_sin_pxr = np.ravel(np.array([array[0, 0, :],  # Píxel superior izquierdo
                           array[0, 1, :],  # Píxel superior derecho
                           array[1, 0, :]])) # Píxel inferior izquierdo
    return imagen_sin_pxr

def separate_colors2(array: list)->tuple[list, list, list]:
    '''
    
    '''
    lista = np.ravel(array)
    rojos = np.ravel(lista)[::3]
    verdes = np.ravel(lista)[1::3]
    azules = np.ravel(lista)[2::3]
    return rojos, verdes, azules

def lesser_variance(array: list)-> list:
    red, green, blue = separate_colors2(array)

    vars_r = np.var(red)
    vars_g = np.var(green)
    vars_b = np.var(blue)

    varianza_menor = min(vars_r, vars_g, vars_b)

    if vars_r == varianza_menor:
        cuadrante_elegido = red.copy()
        indice_color = 0
    elif vars_g == varianza_menor:
        cuadrante_elegido = green.copy()
        indice_color = 1
    elif vars_b == varianza_menor:
        cuadrante_elegido = blue.copy()
        indice_color = 2
    return indice_color, cuadrante_elegido

def desencriptador_imagen(imagen)->list:
    secuencia = []
    matriz_imagen = np.array(imagen)
    alto_imagen, ancho_imagen, _ = get_shape(matriz_imagen)
    for i in range(0, alto_imagen-1, 2):
        for j in range(0, ancho_imagen-1, 2):
            seccion = matriz_imagen[i: i+2, j: j+2, :]
            sin_inf_der = todos_menos_infd(seccion)

            var_minima, color_sin_infd = lesser_variance(sin_inf_der)

            promedio = np.floor(np.mean(color_sin_infd))

            verdadero_valor = (seccion[1, 1, var_minima] - promedio) 
            if verdadero_valor < 0 and verdadero_valor != -1:
                verdadero_valor = (verdadero_valor + 256) 
            secuencia.append(np.int16(verdadero_valor))
            if verdadero_valor == 0:
                break
            else:
                continue
        if verdadero_valor == 0:
            break
    return secuencia

def desencrpitar_mensaje(secuencia)->str:
    for i in range(len(secuencia)):
        if secuencia[i] != -1 and secuencia[i] != 0:
            secuencia[i] = secuencia[i] -1
        elif secuencia[i] == 0:
            break

    mensaje = ""
    nueva_secuencia = []
    
    for numero in secuencia:
        if numero == -1:
            nueva_secuencia.append(int(mensaje))
            mensaje = ""
            nueva_secuencia.append(numero)
        else:
            mensaje += str(numero)

    tabla_numeros_caracteres = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' ', 28: '.',
    29: ',', 30: '?', 31: '!', 32: '¿', 33: '¡', 34: '(', 35: ')', 36: ':', 37: ';',
    38: '-', 39: '“', 40: '‘', 41: 'á', 42: 'é', 43: 'í', 44: 'ó', 45: 'ú', 46: 'ü',
    47: 'ñ'
    }
    mensaje = ''
    for numero in nueva_secuencia:
        if numero == 0:
            break
        elif numero == -1:
            continue
        else:
            caracter = tabla_numeros_caracteres[numero]
            mensaje += caracter
    return mensaje


imagen = np.array(Image.open('encrypted_baboon.png'))
secuencia = desencriptador_imagen(imagen)
print(secuencia)
print(desencrpitar_mensaje(secuencia))