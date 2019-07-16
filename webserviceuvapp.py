from bottle import get,post, run, request
import fcm

#cnZDJimhpGs:APA91bFuVOYE6I0HTWKv7AChnwu55Y97AvmSJ_Ql9sj8bUpaVKl8CU3zNnGrnCCBqIfml7Piht12F73n1tvhBd1C6rv6AAvNIN44ZgZSnxP6grNw2NkhwjMztKUjK4DF7DV4yBEUUxSE

@get('/uvapp/signup') # or @route('/login')
def login():
    return '''
        <form action="/uvapp/signup" method="post">
            Username: <input name="nick" type="text" />
            Token: <input name="token" type="text" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/uvapp/signup') # or @route('/login', method='POST')
def do_login():
    nick = request.forms.get('nick')
    token = request.forms.get('token')
    #guardar en firestore
    #iniciar google cloud platform
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore

    # Use a service account
    cred = credentials.Certificate('uvapp-246400-9e75d4d9608a.json')
    firebase_admin.initialize_app(cred)
    
    db = firestore.client()
    doc_ref = db.collection("usuarios").document( )
    doc_ref.set(       {  "nick": nick, "token": token   })
    #devolver ok
    return "OK"

 


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
    fcm.MyFCM().send_a_notificacion_http_v1()
    #registration_token = request.forms.get('token') 

 


def notificar_apps_pyfcm( token):
    from pyfcm import FCMNotification 
    push_service = FCMNotification( api_key="AIzaSyCNqUp9_KRV9JGLovHiYc87PbSYrWdSZ88")  
    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

    registration_id = token
    message_title = "Uber update"
    message_body = "Hi john, your customized news for today is ready"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

    # Send to multiple devices by passing a list of ids.
    """registration_ids = [ token]
    message_title = "Uber update"
    message_body = "Hope you're having fun this weekend, don't forget to check today's news"
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
    """
    print(result)



def notificar_apps_http(token):
    url="https://fcm.googleapis.com/fcm/send"
    headers = { 'Authorization': 'key=AIzaSyCNqUp9_KRV9JGLovHiYc87PbSYrWdSZ88',  'Content-Type': 'application/json'}
    import requests
    data= {
    "notification":{  "title":"saludo", "body":"how are u" }, 
    "to" : token,
    "data": { "extra": "juice"}
    }
    req = requests.post( url, data=data , headers= headers )
    print( req.status_code)



def notificar_apps( token ):
    # This registration token comes from the client FCM SDKs.
    registration_token = token
    # See documentation on defining a message payload. 
    import firebase_admin
    from firebase_admin import credentials 
    from firebase_admin import messaging
    cred = credentials.Certificate('uvapp-246400-04d67e9d0c21firebasecount.json')
    firebase_admin.initialize_app(  cred) 

    message = messaging.Message(   data={  'score': '850',  'time': '2:45',  }, token=registration_token,)
    # Send a message    to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


@get('/uvapp/notificar')
def get_all():
    tokens= fcm.MyFCM().get_data_from_firestore()

    for ar in tokens:
        #enviar notificacion
        fcm.MyFCM().send_a_notification("Ya son las 9", "Es hora de dormir", ar)
        

 



run(host='192.168.0.12', port=8080)