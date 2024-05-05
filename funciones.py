import numpy as np
from PIL import Image

def add_padding(imagen: list)->list:
    padding = ((2, 2), (2, 2), (0, 0))
    imagen_con_padding = np.pad(imagen, padding, mode='edge')
    return imagen_con_padding