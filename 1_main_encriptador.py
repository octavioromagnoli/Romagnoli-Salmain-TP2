from PIL import Image
import numpy as np
from funciones import encriptador, mensaje_en_imagen, asegurar_extension
#importar funciones (encriptador/desencriptador)

#Encriptacion de Imagen

print('≡≡Encriptador≡≡')
imagen_base = input('Ingrese nombre de la imagen a utilizar como base: ')
imagen_base = asegurar_extension(imagen_base)
imagen_base = np.array(Image.open(imagen_base))
mensaje = input('Ingrese el mensaje a esconder: ')
nombre_archivo_salida = input('Ingrese nombre del archivo de salida: ')
nombre_archivo_salida = asegurar_extension(nombre_archivo_salida)

secuencia = encriptador(mensaje)
imagen_encriptada = mensaje_en_imagen(secuencia, imagen_base)

imagen_encriptada = Image.fromarray(imagen_encriptada.astype('uint8'))
imagen_encriptada.save(nombre_archivo_salida)
print('Imagen encriptada guardada como', nombre_archivo_salida)
