#Trabajo asumiendo que tengo una foto con el padding ya aplicado, uso la funcion padding de funciones y la foto del babuino
import numpy as np
from PIL import Image
from funciones import numpy_image, add_padding, get_shape, var_suma, promedio_colores

#Uso _p como sufijo para las variables que aplican a la imagen con padding
imagen = numpy_image("baboones_fotos/baboonoriginal.png")
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
            cuadrante_elegido = cuad_c[:,:,:].copy()

        pixel_resultante = promedio_colores(cuadrante_elegido)

        copia_img_padding[fila_real][columna_real] = pixel_resultante

        #print(cuadrante_elegido.shape)
        #rojos_a, verdes_a, azules_a = separate_colors(cuad_a)

imagen_kuwahara = copia_img_padding[2:-2,2:-2,:]
Image.fromarray(imagen_kuwahara).save('foto_resultantex.png')
imagen_objetivo = numpy_image("baboones_fotos/kuwahara_baboon.png")

print(f'shape kuwa: {imagen_kuwahara.shape}')
print(f'shape objetivo: {imagen_objetivo.shape}')

son_iguales = True
son_iguales = np.array_equal(imagen_kuwahara, imagen_objetivo)

if son_iguales:
    print("Las dos imágenes son exactamente iguales.")
else:
    print("Las dos imágenes no son iguales.")


