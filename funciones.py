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
