from bottle import get,post,delete, run, request,response
import fcm

#cnZDJimhpGs:APA91bFuVOYE6I0HTWKv7AChnwu55Y97AvmSJ_Ql9sj8bUpaVKl8CU3zNnGrnCCBqIfml7Piht12F73n1tvhBd1C6rv6AAvNIN44ZgZSnxP6grNw2NkhwjMztKUjK4DF7DV4yBEUUxSE

 

@get('/uvapp/signup') # or @route('/login')
def login():
    
    return '''
        <form action="/uvapp/signup" method="post" >
            Username: <input name="nick" type="text" />
            Token: <input name="token" type="text" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/uvapp/signup') # or @route('/login', method='POST')
def do_login(): 
    nick= ""
    token=""
    if request.json != None:
        data= request.json
        nick = data['nick']
        token = data['token']
    else:
        data=   request.forms
        nick = data.get("nick")
        token = data.get("token")

    response.content_type = 'application/json' 
    return fcm.MyFCM().add_data_to_firestore( { "nick": nick, "token": token  }  )


@get('/uvapp/delete/<nick>')
def delete_user( nick):
    return fcm.MyFCM().del_data_to_firestore( nick )




@get('/uvapp/users/all')
def get_all_users():
    fcm.MyFCM().get_data_from_firestore()


@get('/uvapp/notificar/<iuv:int>')
def send_messages_to_all(iuv):
    fcm.MyFCM().messaging_from_firestore(   iuv )


 
 ### PRUEBAS

@get('/uvapp/notificar2')
def send_messages_to_all2():
    fcm.MyFCM().messaging_from_firestore2()


@get('/msg') # or @route('/login')
def single_message_get():
    return '''
        <form action="/msg" method="post"> 
            token: <input name="token" type="text" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/msg') # or @route('/login', method='POST')
def single_message_post(): 
    registration_token = request.forms.get('token') 
    fcm.MyFCM().send_a_notificacion_http_v1( registration_token)



run(host='192.168.0.12', port=8080)