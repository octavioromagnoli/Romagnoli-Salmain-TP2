#Trabajo asumiendo que tengo una foto con el padding ya aplicado, uso la funcion padding de funciones y la foto del babuino
import numpy as np
from PIL import Image
from funciones import apply_kuwahara

if __name__ == "__main__":
    imagen_procesada = apply_kuwahara("baboones_fotos/baboonoriginal.png")
    Image.fromarray(imagen_procesada).save('result_apply_filter.png')

