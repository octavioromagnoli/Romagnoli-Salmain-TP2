import numpy as np
from PIL import Image

#Función que abre la imagen y la convierte en array de numpy
def numpy_image(path: str)->list:
    '''
    Abre la imagen y la convierte a un array numpy de pixeles.
    Utiliza numpy e Image de Pillow.
    Argumentos:
        path: str
            path a la imagen que se quiere convertir a array
    Devuelve:
        np.array de tres dimensiones que representa la imagen
    '''
    imagen_pil = Image.open(path)
    array_imagen = np.array(imagen_pil, dtype=np.uint8)
    return array_imagen

def get_shape(array: list)->tuple[int, int, int]:
    '''
    Toma un array y devuelve una tupla con los largos de cada dimension
    Argumentos:
        array : np.array
            El array del que se quiere saber la forma
    Devuelve:
        La forma del array en formato tupla como (alto, largo, dimensiones)
    '''
    return array.shape

#Función que añade padding a la imagen
def add_padding(imagen: list)->list:
    '''
    Agrega padding de 2 pixeles a una imagen copiando los valores del borde.
    Argumentos:
        Imagen: np.array
            Array de pixeles de la imagen a la que se le quiere agregar padding
    Devuelve:
        Array de la imagen con el padding añadido
    '''
    padding = ((2, 2), (2, 2), (0, 0))
    imagen_con_padding = np.pad(imagen, padding, mode='edge')
    return imagen_con_padding

def separate_colors(array: list)->tuple[list, list, list]:
    '''
    Separa las tres dimensiones de color de un array tipo imagen en tres
    arrays diferentes para Rojo, Verde y Azul.
    Argumentos:
        array: np.array
            El array de la imagen de la cual se quieren separar las dimensiones de color.
    Devuelve:
        Tupla con los arrays de la dimension de Rojo, Verde y Azul
    '''
    rojos = array[:,:,0]
    verdes = array[:,:,1]
    azules = array[:,:,2]
    return rojos, verdes, azules

def var_suma(array: list)->int:
    '''
    Toma un array y devuelve la suma de las varianzas de cada color en ese array.
    Usa la funcion separate_colors()
    Argumentos:
        array : np.array
            El array del cual se quiere obtener la varianza por color
    Devuelve:
        Int de la suma de los valores de varianza de Rojo, Verde y azul.
    '''
    rojos, verdes, azules = separate_colors(array)
    var_roj = rojos.var()
    var_ver = verdes.var()
    var_azu = azules.var()
    suma = var_roj + var_ver + var_azu
    return suma

def promedio_colores(array: list)->list[int, int, int]:
    '''
    Toma un array imagen (tridimensional) y devuelve el resultado del promedio de sus colores.
    Usa la funcion separate_colors()
    Argumentos:
        array : list
            el array del cual se quieren calcular los promedios de color
    Devuelve:
        np.array con los promedios de rojo, verde y azul del array en formato de pixel
    '''
    rojos, verdes, azules = separate_colors(array)
    prom_rojo = np.mean(rojos)
    prom_verde = np.mean(verdes)
    prom_azul = np.mean(azules)

    return np.array([prom_rojo, prom_verde, prom_azul], dtype=np.uint8)

def todos_menos_infd(array:list)->list:
    '''
    Esta función excluye el pixel inferior derecho de una matriz de 2x2.
    Luego toma esos valores y los concatena en una lista unidimensional.
    Argumentos:
        array : list
            np.array de shape (2,2,x) al cual se le quiere extraer el pixel inferior derecho.
    Devuelve:
        Lista con los valores de cada pixel concatenados.
        En caso de ser pixeles RGB, cada 3 valores se repite el color
        (r, g, b, r2, g2, b2, r3, etc...)
    '''
    imagen_sin_pxr = np.ravel(np.array([array[0, 0, :],  # Píxel superior izquierdo
                           array[0, 1, :],  # Píxel superior derecho
                           array[1, 0, :]])) # Píxel inferior izquierdo
    return imagen_sin_pxr

def separate_colors2(array: list)->tuple[list, list, list]:
    '''
    Separa los colores pero devuelve los valores en una lista unidimensional.
    Argumentos:
        array : list
            La lista de pixeles de la cual se quieren separar los colores.
    Devuelve:
        Tupla con las listas que contienen los valores de cada color en cada pixel.
    '''
    lista = np.ravel(array)
    rojos = np.ravel(lista)[::3]
    verdes = np.ravel(lista)[1::3]
    azules = np.ravel(lista)[2::3]
    return rojos, verdes, azules

def lesser_variance(array: list)-> list:
    '''
    Calcula el color de menor varianza en un array. Para separar los colores utiliza separate_colors2().
    Argumentos:
        array : list
            El array del cual se quiere saber el color con menor varianza.
    Devuelve:
        indice_color : int
            Un int entre 0 y 2 inclusive que representa el indice de color RGB del color que presenta
            menor varianza.
        cuadrante_elegido : list
            Lista con los valores del color con menor varianza en el array.
    '''
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


def encriptador(mensaje: str)->list: 
    '''
    Esta funcion encripta un mensaje y lo convierte en la secuencia que utiliza mensaje_en_imagen().
    Argumentos:
        mensaje : str
            El mensaje que quiere ser traducido a secuencia de encriptacion
    Devuelve:
        lista con la secuencia de numeros representante del mensaje encriptado.
    '''
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
    
def mensaje_en_imagen(secuencia: list,imagen: list)->list[list[list]]:
    '''
    Esta funcion toma la secuencia dada y la esconde en los pixeles de la imagen que se desee.
    Argumentos:
        secuencia : list
            la secuencia representante del mensaje encriptado que se quiere esconder en la imagen.
        imagen : np.array
            numpy array de la foto en la cual se quiere esconder el mensaje
    Devuelve:
        array de la imagen con el mensaje encriptado oculto en ella.
    '''

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


def desencriptador_imagen(imagen: str)->list:
    '''
    Esta funcion toma la imagen encriptada y "saca" la secuencia del mensaje oculto en ella.
    Argumentos:
        imagen : str
            el path a la imagen que contiene el mensaje y de la cual se quiere extraer la secuencia.
    Devuelve:
        Lista con la secuencia de numeros que representa el mensaje oculto.
    '''
    secuencia = []
    matriz_imagen = numpy_image(imagen)
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

def desencrpitar_mensaje(secuencia: list)->str:
    '''
    Esta funcion interpreta la secuencia del mensaje encriptado.
    Argumentos:
        secuencia : list
            lista de numeros representante del mensaje encriptado
    Devuelve:
        String con el mensaje obtenido de la secuencia.
    '''
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


def apply_kuwahara(path: str)->list:
    '''
    Esta funcion recibe el path a una imagen y devuelve la matriz numpy de la imagen con el filtro Kuwahara aplicado.
    Utiliza las funciones: numpy_image, add_padding, get_shape, var_suma, promedio_colores (del archivo funciones.py).
    Argumentos:
        path : str
            path al archivo de tipo Imagen al cual se le quiere aplicar el filtro kuwahara.
    Devuelve:
        La Imagen ya con el filtro aplicado como np.array tridimensional.
    '''

    #Uso _p como sufijo para las variables que aplican a la imagen con padding
    imagen = numpy_image(path)
    imagen_padding = add_padding(imagen)
    copia_img_padding = imagen_padding[:,:,:].copy()
    filas_p, columnas_p, dimensiones_p = get_shape(imagen_padding)


    #Los for anidados hacen que lopee en los pixeles de la imagen real dentro de la imagen con padding
    for fila_real in range(2, filas_p - 2):
        for columna_real in range(2, columnas_p - 2):
            cuad_a = imagen_padding[fila_real-2:fila_real+1, columna_real-2:columna_real+1, :]
            cuad_b = imagen_padding[fila_real-2:fila_real+1, columna_real:columna_real+3, :]
            cuad_c = imagen_padding[fila_real:fila_real+3, columna_real-2:columna_real+1, :]
            cuad_d = imagen_padding[fila_real:fila_real+3, columna_real:columna_real+3, :]
            
            vars_a = var_suma(cuad_a)
            vars_b = var_suma(cuad_b)
            vars_c = var_suma(cuad_c)
            vars_d = var_suma(cuad_d)

            varianza_menor = min(vars_a, vars_b, vars_c, vars_d)

            if vars_a == varianza_menor:
                cuadrante_elegido = cuad_a[:,:,:].copy()
            elif vars_b == varianza_menor:
                cuadrante_elegido = cuad_b[:,:,:].copy()
            elif vars_c == varianza_menor:
                cuadrante_elegido = cuad_c[:,:,:].copy()
            elif vars_d == varianza_menor:
                cuadrante_elegido = cuad_d[:,:,:].copy()

            pixel_resultante = promedio_colores(cuadrante_elegido)

            copia_img_padding[fila_real, columna_real] = pixel_resultante

            #print(cuadrante_elegido.shape)
            #rojos_a, verdes_a, azules_a = separate_colors(cuad_a)

    imagen_kuwahara = copia_img_padding[2:-2,2:-2,:].copy()

    return imagen_kuwahara


def asegurar_extension(nombre_archivo: str)->str:
    '''
    Esta funcion se asegura de que el nombre del archivo tenga la extension '.png'.
    Argumentos:
        nombre_archivo : str
            string que se quiere que termine en .png
    Devuelve:
        El str con .png al final si no tenia la extension, si no no modifica nada.
    '''
    if not nombre_archivo.endswith(".png"):
        nombre_archivo += ".png"
    return nombre_archivo
