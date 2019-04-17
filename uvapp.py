from bottle import get,post, run, request, template
import os
import cv2
import Fototipo_detect


@get("/name")
def show_name():
    from bottle import response
    from json import dumps
    rv = { "code": 1994 }
    response.content_type = 'application/json'
    return dumps(rv) 



@get('/phototype')
def index():
    return "<form action='/phototype'  method='post' enctype='multipart/form-data'> <input type='file' name='foto' /> <input type='submit' value='send' /> </form>"


@post('/phototype')
def receive(): 

    import bottle
    from bottle import response, request
    bottle.BaseRequest.MEMFILE_MAX = 1024*1024*1024*1024
    from json import dumps  

    upload=	request.files.get("foto")
    filename= upload.filename
    name, ext = os.path.splitext( filename)

    if ext not in ('.png','.jpg','.jpeg'):

        rv = { "estado": 400 }
        response.content_type = 'application/json'
        return dumps(rv) 

    else:
        upload.save("./")
	################
	#recortar imagen
        """filename_crop= name+"_crop"+ext
        img= cv2.imread( filename)
        crop_img = img[1200:1290, 1000:1090]
        #suavizar
        #Crea el kernel
        import numpy as np
        kernel = np.ones((5,5),np.float32)/50
        #Filtra la imagen utilizando el kernel anterior
        dst = cv2.filter2D( crop_img,-1,kernel)
        cv2.imwrite( filename_crop , dst)
        """

	################
        #leer archivo
        read_img= Fototipo_detect.Fototipo_detect( filename  ) 
        intensidad= read_img.determ_phototype()


	################
        #borrar archivo
        from os import remove
        remove( filename)
	#remove( filename)

        rv = { "phototype": intensidad , "estado": 200}

        response.content_type = 'application/json'
        return dumps(rv)


run(host='192.168.0.12', port=8080)