from PIL import Image
import numpy as np
from funciones import desencrpitar_mensaje, desencriptador_imagen
#importar funciones (encriptador/desencriptador)


#Desencriptacion de Imagen

print('≡≡Desencriptador≡≡')
nombre_archivo_encriptado = input("Ingrese nombre del archivo encriptado (.png): ")

secuencia = desencriptador_imagen(nombre_archivo_encriptado)
mensaje_oculto = desencrpitar_mensaje(secuencia)

print("El mensaje oculto es:", mensaje_oculto)
