from PIL import Image
import numpy as np
#importar funciones (encriptador/desencriptador)

def asegurar_extension(nombre_archivo):
    if not nombre_archivo.endswith(".png"):
        nombre_archivo += ".png"
    return nombre_archivo

#Encriptacion de Imagen

print('≡≡Encriptador≡≡')
imagen_base = input('Ingrese nombre de la imagen a utilizar como base: ')
imagen_base = asegurar_extension(imagen_base)
mensaje = input('Ingrese el mensaje a esconder: ')
nombre_archivo_salida = input('Ingrese nombre del archivo de salida: ')
nombre_archivo_salida = asegurar_extension(nombre_archivo_salida)

secuencia = encriptador(mensaje)
imagen_encriptada = mensaje_en_imagen(secuencia, imagen_base)

imagen_encriptada = Image.fromarray(imagen_encriptada.astype('uint8'))
Image.open(imagen_encriptada)
imagen_encriptada.save(nombre_archivo_salida)
print('Imagen encriptada guardada como', nombre_archivo_salida)

#Desencriptacion de Imagen

print('≡≡Desencriptador≡≡')
nombre_archivo_encriptado = input("Ingrese nombre del archivo encriptado (.png): ")

secuencia = desencriptar_imagen(nombre_archivo_encriptado)
mensaje_oculto = desencriptar_mensaje(secuencia)

print("El mensaje oculto es:", mensaje_oculto)
