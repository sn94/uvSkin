import cv2
import numpy as np
from matplotlib import pyplot as plt

from os import listdir


class Uvapp_find_pho:


    #Escala cromatica de Von Luschan
    #Codigo de colores representativos para cada tono de piel 
    croma_list= [ [ 244,242,245], [236,235,233], [250,249,247],[253,251,230],[253,246,230],[254,247,229],[250,240,239],[243,234,229],[244,241,234] ,
                [251,252,244],[252,248,237],[254,246,225],[255,249,225],[245,239,215],[241,231,195],[239,226,173],[224,210,147],[242,226,151],
                [235,214,159],[235,217,133],[227,196,103],[225,193,106],[223,193,123],[222,184,119],[199,164,100],[188,151,98],[156,107,67] ,
                [142,88,62],[121,77,48],[100,49,22],[101,48,32],[96,49,33],[87,50,41],[64,32,21],[49,37,41],[27,28,46] ]
    
    fototipo_croma= { 1: [1,2,3,4,5], 2: [6,7,8,9,10], 3: [11,12,13,14,15], 4:[16,17,18,19,20,21], 5:[22,23,24,25,26,27,28], 6:[29,30,31,32,33,34,35,36] }

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
 