

class MyFCM:


    def __init__(self):
        pass
    

    def _get_access_token(self):
        """Retrieve a valid access token that can be used to authorize requests.
        :return: Access token.
        """
        #'uvapp-246400-6c35cea9bf32default.json'
        from oauth2client import service_account
        credentials = service_account.ServiceAccountCredentials.from_json_keyfile_name(
            'uvapp-246400-6c35cea9bf32default.json', "https://www.googleapis.com/auth/firebase.messaging")
        access_token_info = credentials.get_access_token()
        return access_token_info.access_token


    def send_a_notificacion_http_v1(self, token, iuv   ):
        print(  token)
        url="https://fcm.googleapis.com/v1/projects/uvapp-246400/messages:send"
        headers = { 'Authorization': 'Bearer '+self._get_access_token(),  
        'Content-Type': 'application/json; UTF-8'}
        import requests, json
        msgtext=  "iuv alto "+ str( iuv)
        data= { 'message':
        {
        "notification": { "title": "Atencion!!","body": msgtext},
        "data": { "story_id": "story_12345"}  , 
        "token":  token,
        } }
        
        req = requests.post( url, data= json.dumps( data) , headers= headers )
        print( req.status_code, req)




#'cnZDJimhpGs:APA91bFuVOYE6I0HTWKv7AChnwu55Y97AvmSJ_Ql9sj8bUpaVKl8CU3zNnGrnCCBqIfml7Piht12F73n1tvhBd1C6rv6AAvNIN44ZgZSnxP6grNw2NkhwjMztKUjK4DF7DV4yBEUUxSE'
    def send_a_notification_sdk_admin( self, title, body, token ):
        registration_token = token
        # See documentation on defining a message payload. 
        import firebase_admin
        from firebase_admin import credentials 
        from firebase_admin import messaging 
        cred = credentials.RefreshToken( 'uvapp-246400-04d67e9d0c21firebasecount.json')
        #cred = credentials.Certificate('mensajeador-5822102cebdc.json')
        app=firebase_admin.initialize_app(  cred)
        a_notification = messaging.Notification (  title= title, body=  body)
        message = messaging.Message(  data= None, notification=a_notification,  token=registration_token,)
        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
        firebase_admin.delete_app(  app )#borrar instancia anterior



    def send_a_data_message_sdk_admin(self, title, body, token ): 
        registration_token = token
        # See documentation on defining a message payload. 
        import firebase_admin
        from firebase_admin import credentials 
        from firebase_admin import messaging
        cred = credentials.Certificate('uvapp-246400-04d67e9d0c21firebasecount.json')
        app= firebase_admin.initialize_app(  cred)   
        message = messaging.Message( data={  'score': '850',  'time': '2:45',  },   token=registration_token) 
        response = messaging.send(message) 
        print('Successfully sent message:', response)
        firebase_admin.delete_app(  app )#borrar instancia anterior



    def add_data_to_firestore(self, params):
        if self.exist_nick(  params['nick'] ):
            return {"estado": 400, "msg": "NICK YA REGISTRADO!" }
        else:
            #guardar en firestore
            #iniciar google cloud platform
            import firebase_admin
            from firebase_admin import credentials
            from firebase_admin import firestore
            # Use a service account
            cred = credentials.Certificate('uvapp-246400-9e75d4d9608a.json')
            app= firebase_admin.initialize_app(cred)
            db = firestore.client()
            doc_ref = db.collection("usuarios").document( )
            doc_ref.set(       {  "nick": params['nick'], "token": params['token']   })
            firebase_admin.delete_app(  app )#borrar instancia anterior 
            #devolver ok
            return {"estado": 200, "msg": "USUARIO CREADO!" }

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
        app= firebase_admin.initialize_app(   cred )
        
        db = firestore.client() 
        users_ref = db.collection(u'usuarios')
        docs = users_ref.get()
        for doc in docs:
            #registro_id= doc.id
            registro_user=doc.to_dict()
            print( registro_user )
        firebase_admin.delete_app(   app )#borrar instancia anterior
        
    def exist_nick(self, nick):
        #guardar en firestore
        #iniciar google cloud platform
        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import firestore
        # Use a service account
        cred = credentials.Certificate('uvapp-246400-9e75d4d9608a.json')
        app= firebase_admin.initialize_app(cred)
        db = firestore.client()
        usu_ref = db.collection("usuarios")
        users_ref= usu_ref.where( 'nick' , '==', nick )
        docs = users_ref.get()
        firebase_admin.delete_app(  app )#borrar instancia anterior 
       
        try:
            next( docs)
            print("existe")
            return True
        except:
            print("NO existe")
            return False



    def del_data_to_firestore(self, nick):
        if not self.exist_nick(  nick ):
            return {"estado":400, "msg": "NO EXISTE ESE NICK"}
        else:
            #guardar en firestore
            #iniciar google cloud platform
            import firebase_admin
            from firebase_admin import credentials
            from firebase_admin import firestore
            # Use a service account
            cred = credentials.Certificate('uvapp-246400-9e75d4d9608a.json')
            app= firebase_admin.initialize_app(cred)
            db = firestore.client()
            usu_ref = db.collection("usuarios")
            users_ref= usu_ref.where( 'nick' , '==', nick )
            docs = users_ref.get()
            for doc in docs:
                doc.reference.delete() 
                
            firebase_admin.delete_app(  app )#borrar instancia anterior 
            #devolver ok
            return {"estado": 200, "msg": "USUARIO BORRADO!" }


    def messaging_from_firestore(self,  iuv   ):
        #consulta lo de cloud firestore
        # Use a service account
        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import firestore   

        #cred = credentials.Certificate('uvapp-246400-9e75d4d9608a.json')
        #'uvapp-246400-04d67e9d0c21firebasecount.json'
        #'uvapp-246400-6c35cea9bf32default.json
        cred = credentials.Certificate( 'uvapp-246400-04d67e9d0c21firebasecount.json' )
        app= firebase_admin.initialize_app(   cred )
        
        db = firestore.client() 
        users_ref = db.collection(u'usuarios')
        docs = users_ref.get()  
        
        for doc in docs:
            #registro_id= doc.id
            registro_user=doc.to_dict()
            token=  registro_user['token']  
            self.send_a_notificacion_http_v1( token , iuv  )
        firebase_admin.delete_app(   app )#borrar instancia anterior
        

    def messaging_from_firestore2(self ):
        #consulta lo de cloud firestore
        # Use a service account
        import firebase_admin
        from firebase_admin import credentials

        #cred = credentials.Certificate('uvapp-246400-9e75d4d9608a.json')
        #'uvapp-246400-04d67e9d0c21firebasecount.json'
        #'uvapp-246400-6c35cea9bf32default.json
        cred = credentials.Certificate( 'uvapp-246400-04d67e9d0c21firebasecount.json' ) 
        app= firebase_admin.initialize_app(   cred )

        from firebase_admin import firestore   
        db = firestore.client() 
        users_ref = db.collection(u'usuarios')
        docs = users_ref.get() 
        
        from firebase_admin import messaging
        for doc in docs:
            #registro_id= doc.id
            registro_user=doc.to_dict()
            token=  registro_user['token']  
            a_notification = messaging.Notification (  title= "hola", body=  "quetal")
            message = messaging.Message(  data= None, notification=a_notification,  token=token)
            # Send a message to the device corresponding to the provided
            # registration token.
            response = messaging.send(message)
            # Response is a message ID string.
            print('Successfully sent message:', response)
            #self.send_a_notification_sdk_admin( "iuv alto","cuidate",token )
        firebase_admin.delete_app(   app )#borrar instancia anterior