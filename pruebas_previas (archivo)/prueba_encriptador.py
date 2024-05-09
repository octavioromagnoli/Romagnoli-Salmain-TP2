from PIL import Image
import numpy as np
from funciones import encriptador, mensaje_en_imagen



if __name__ == '__main__':
    mensaje = 'le pongo un mensaje a mi babun'
    secuencia = encriptador(mensaje)
    imagen = np.array(Image.open('baboones_fotos/kuwahara_baboon.png'))
    mensaje_encriptado = mensaje_en_imagen(secuencia, imagen)
    print(secuencia)
    print(mensaje_encriptado)
    imagen = Image.fromarray(mensaje_encriptado.astype('uint8'))
    imagen.save('babun_encriptado.png')
