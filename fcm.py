

class MyFCM:


    def __init__(self):
        pass
    

    def _get_access_token(self):
        """Retrieve a valid access token that can be used to authorize requests.
        :return: Access token.
        """
        from oauth2client import service_account
        credentials = service_account.ServiceAccountCredentials.from_json_keyfile_name(
            'uvapp-246400-6c35cea9bf32default.json', "https://www.googleapis.com/auth/firebase.messaging")
        access_token_info = credentials.get_access_token()
        return access_token_info.access_token


    def send_a_notificacion_http_v1(self):
       
        url="https://fcm.googleapis.com/v1/projects/uvapp-246400/messages:send"
        headers = { 'Authorization': 'Bearer '+self._get_access_token(),  
        'Content-Type': 'application/json; UTF-8'}
        import requests, json
        data= { 'message':
        {
        'notification': { 'title': 'Breaking News','body': 'New news story available.'},
        'data': { 'story_id': 'story_12345'}  , 
        'token':'cnZDJimhpGs:APA91bFuVOYE6I0HTWKv7AChnwu55Y97AvmSJ_Ql9sj8bUpaVKl8CU3zNnGrnCCBqIfml7Piht12F73n1tvhBd1C6rv6AAvNIN44ZgZSnxP6grNw2NkhwjMztKUjK4DF7DV4yBEUUxSE'
        } }
        req = requests.post( url, data= json.dumps( data) , headers= headers )
        print( req.status_code, req)


    def send_a_notification( self, title, body, token ):
        registration_token = token
        # See documentation on defining a message payload. 
        import firebase_admin
        from firebase_admin import credentials 
        from firebase_admin import messaging
        #https://www.googleapis.com/auth/cloud-platform
        #cred = credentials.RefreshToken( 'uvapp-246400-04d67e9d0c21firebasecount.json')
        
    
        cred = credentials.Certificate('mensajeador-5822102cebdc.json')
        firebase_admin.initialize_app(  cred)
        a_notification = messaging.Notification (  title= title, body=  body)
        message = messaging.Message(  data= None, notification=a_notification,  token=registration_token,)
        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)



    def send_a_data_message(self, title, body, token ): 
        registration_token = token
        # See documentation on defining a message payload. 
        import firebase_admin
        from firebase_admin import credentials 
        from firebase_admin import messaging
        cred = credentials.Certificate('uvapp-246400-04d67e9d0c21firebasecount.json')
        firebase_admin.initialize_app(  cred)   
        message = messaging.Message( data={  'score': '850',  'time': '2:45',  },   token=registration_token) 
        response = messaging.send(message) 
        print('Successfully sent message:', response)



    def get_data_from_firestore(self ):
        #consulta lo de cloud firestore
        # Use a service account
        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import firestore  
        from firebase_admin import messaging

        #cred = credentials.Certificate('uvapp-246400-9e75d4d9608a.json')
        #'uvapp-246400-04d67e9d0c21firebasecount.json'
        #'uvapp-246400-6c35cea9bf32default.json
        cred = credentials.Certificate( 'uvapp-246400-04d67e9d0c21firebasecount.json' )
        firebase_admin.initialize_app(   cred )
        
        db = firestore.client() 
        users_ref = db.collection(u'usuarios')
        docs = users_ref.get() 
        firebase_admin.delete_app(   firebase_admin.get_app() )#borrar instancia anterior
        tokens=[] 
        for doc in docs:
            #registro_id= doc.id
            registro_user=doc.to_dict()
            token=  registro_user['token'] 
            tokens.append(  token) 

            
        return tokens