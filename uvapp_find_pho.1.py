import cv2
import numpy as np
from matplotlib import pyplot as plt

from os import listdir


class Uvapp_find_pho:


    # TONOS  MUY CLARO CLARO  MEDIO   OSCURO    
    tonos= [(255,94),(95,64),(63,32), (31,0)]
    tono_txt= {0:'MUY CLARO', 1:'CLARO', 2:'MEDIO',3:'OSCURO'}

    def calc_int_promedio( self, img):
        return (img.sum()/2) / img.size

    def procesar_imagen(self,  img): 
        img_arr = cv2.imread( img , cv2.IMREAD_GRAYSCALE)
        intensidad= int(   round( self.calc_int_promedio(  img_arr) )  )
        indexTone= 0
        for a in self.tonos:
            max,min= a
            if( intensidad >= min and  intensidad <= max):
                break
            indexTone+= 1
        mandar= self.tono_txt.get( indexTone, lambda: "ERROR")
        return  mandar
 