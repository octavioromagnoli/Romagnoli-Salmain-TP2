from PIL import Image
import numpy as np
from funciones import  desencriptador_imagen, desencrpitar_mensaje

if __name__ == '__main__':
    imagen = 'babun_encriptado.png'
    secuencia = desencriptador_imagen(imagen)
    print(secuencia)
    print(desencrpitar_mensaje(secuencia))