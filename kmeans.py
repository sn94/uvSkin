import matplotlib.pyplot as plt  
import numpy as np  
from sklearn.cluster import KMeans 

import cv2 #for resizing image


class Fototipo_detect:


    #Escala cromatica de Von Luschan
    #Codigo de colores representativos para cada tono de piel 
    croma_list= [ [ 244,242,245], [236,235,233], [250,249,247],[253,251,230],[253,246,230],[254,247,229],[250,240,239],[243,234,229],[244,241,234] ,
                [251,252,244],[252,248,237],[254,246,225],[255,249,225],[245,239,215],[241,231,195],[239,226,173],[224,210,147],[242,226,151],
                [235,214,159],[235,217,133],[227,196,103],[225,193,106],[223,193,123],[222,184,119],[199,164,100],[188,151,98],[156,107,67] ,
                [142,88,62],[121,77,48],[100,49,22],[101,48,32],[96,49,33],[87,50,41],[64,32,21],[49,37,41],[27,28,46] ]
    
    fototipo_croma= { 1: [1,2,3,4,5], 2: [6,7,8,9,10], 3: [11,12,13,14,15], 4:[16,17,18,19,20,21], 5:[22,23,24,25,26,27,28], 6:[29,30,31,32,33,34,35,36] }

    distancias_eu= []


    def __init__( self, ruta):
        #leer imagen
        img_arr = cv2.imread( ruta )
        b,g,r = cv2.split( img_arr )       # get b,g,r
        self.X = cv2.merge([r,g,b])     # switch it to rgb
        import dominant_color
        self.color_dominante= dominant_color.get_dominant_color(  self.X,  k=4, image_processing_size= ( self.X.shape[0], self.X.shape[1])  )


    def color_euclidean_distance( self,  color_rgb, color_rgb2):
        #https://lmcaraig.com/color-quantization-using-k-means/
        r_dif=  pow(  (color_rgb[0]-color_rgb2[0])  , 2)
        g_dif=  pow(  (color_rgb[1]-color_rgb2[1]), 2)
        b_dif=  pow(  (color_rgb[2]-color_rgb2[2]), 2)
        import math
        raiz= math.sqrt(  r_dif+ g_dif+ b_dif ) 
        return raiz



    def calculate_distances( self ):
        for index in range(0, len( self.croma_list )    ):
            color= self.croma_list[index] 
            distancia=  self.color_euclidean_distance( color, self.color_dominante  )
            self.distancias_eu.insert( index, {"index": index, "distancia": distancia}) 

            
    def coord_von_luschan_color(self):
        newlist= sorted(  self.distancias_eu,  key=  lambda d:   d["distancia"]  )
        return newlist[0]['distancia']



import time

ini=time.time()
ff= Fototipo_detect( "red.png")
ff.calculate_distances()
print(ff.coord_von_luschan_color() ) 
fin=time.time()
print( fin-ini, "sec")

