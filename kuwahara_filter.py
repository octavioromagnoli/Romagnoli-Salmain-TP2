#Trabajo asumiendo que tengo una foto con el padding ya aplicado, uso la funcion padding de funciones y la foto del babuino
import numpy as np
from PIL import Image
from funciones import numpy_image, add_padding, get_shape, var_suma, promedio_colores

def apply_kuwahara(path: str)->list:
    '''
    Este filtro aplica el filtro Kuwahara a una imagen.
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

if __name__ == "__main__":
    imagen_procesada = apply_kuwahara("baboones_fotos/baboonoriginal.png")
    Image.fromarray(imagen_procesada).save('foto_resultante.png')

