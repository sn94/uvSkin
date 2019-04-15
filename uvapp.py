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
        #leer archivo
        read_img= Fototipo_detect.Fototipo_detect( filename   ) 
        intensidad= read_img.determ_phototype()
        #borrar archivo
        from os import remove
        remove( filename)
        rv = { "tone": intensidad , "estado": 200}

        response.content_type = 'application/json'
        return dumps(rv)


run(host='192.168.0.12', port=8080)