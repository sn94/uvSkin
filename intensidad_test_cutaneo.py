import cv2
import numpy as np
from matplotlib import pyplot as plt

from os import listdir



# TONOS  MUY CLARO CLARO  MEDIO   OSCURO    
tonos= [(255,94),(95,64),(63,32), (31,0)]

def calc_int_promedio( img):
    return (img.sum()/2) / img.size

def procesar_muestras():
    for img in listdir("Tonalidades"):
        img_arr = cv2.imread(  "Tonalidades/"+img , cv2.IMREAD_GRAYSCALE)
        intensidad= calc_int_promedio(  img_arr)
        print(   img, intensidad)


def procesar_imagen( img): 
    img_arr = cv2.imread( img , cv2.IMREAD_GRAYSCALE)
    intensidad= calc_int_promedio(  img_arr)
    print(   img, intensidad)

procesar_muestras()
"""
img = cv2.imread('mipiel_negra.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('mipiel_negra.jpg', img)

np.set_printoptions( threshold= np.NaN)

print(img.sum()/ img.size) #promedio 127.38
# 58.9 piel negra valores mas bajos de intensidad

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()"""