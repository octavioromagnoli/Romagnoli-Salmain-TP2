import numpy as np
from PIL import Image

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