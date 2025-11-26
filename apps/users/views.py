from rest_framework.authtoken.views import ObtainAuthToken # Importar la vista base para obtener tokens
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token # Importar el modelo Token

from apps.users.api.serializers import UserTokenSerializer # Importar el serializador de usuario para la respuesta

from django.contrib.sessions.models import Session

from datetime import datetime
from rest_framework.views import APIView

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        # Validar las credenciales del usuario usando el serializer de autenticación
        login_serializer = self.serializer_class(data=request.data, context ={'request': request})
        
        # Verificar si las credenciales son válidas
        if login_serializer.is_valid():
            # Obtener el usuario validado
            user = login_serializer.validated_data['user']
            
            # Verificar si el usuario está activo
            if user.is_active:
                # Obtener o crear un token para el usuario
                token, created = Token.objects.get_or_create(user=user)
                
                # Serializar los datos del usuario para la respuesta
                user_serializer = UserTokenSerializer(user)
                
                # Si el token fue recién creado
                if created:
                    return Response({
                        'token': token.key,  # Clave del token para autenticación
                        'user': user_serializer.data,  # Datos del usuario
                        'message': 'Inicio de sesión exitoso. Token creado.'
                    }, status=status.HTTP_201_CREATED)
                    
                else:
                    """# Eliminar todas las sesiones activas del usuario en el rango de tiempo
                    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    # Buscar y eliminar sesiones del usuario
                    if all_sessions.exists():
                        # Iterar sobre las sesiones activas
                        for session in all_sessions:
                            # Decodificar los datos de la sesión
                            session_data = session.get_decoded()
                            # Verificar si la sesión pertenece al usuario actual
                            if user.id == int(session_data.get('_auth_user_id')):
                                # Eliminar la sesión 
                                session.delete()
                    # Si el token ya existía, eliminarlo para generar uno nuevo
                    token.delete()
                    # Crear un nuevo token para el usuario
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,  # Nueva clave del token
                        'user': user_serializer.data,  # Datos del usuario
                        'message': 'Inicio de sesión exitoso. Token renovado.'
                    }, status=status.HTTP_201_CREATED)"""
                    token.delete()
                    return Response({
                        'error': 'Ya existe una sesión activa para este usuario. Cierre la sesión en otro dispositivo antes de iniciar una nueva.'
                    }, status=status.HTTP_409_CONFLICT)
                    
            #end if
            else:
                # Usuario existe pero está inactivo
                return Response({'error': 'Usuario inactivo'}, status=status.HTTP_403_FORBIDDEN)
            #end else
        #end if
        else:
            # Credenciales incorrectas (usuario o contraseña inválidos)
            return Response({'error': 'Credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)
        #end else   

class Logout(APIView):
    def get(self, request, *args, **kwargs):
        
        try:
            token = request.Get.get('token')
            token = Token.objects.filter(key=token).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                
                token.delete()
                
                session_message = 'Sesiones de usuario eliminadas'
                token_message = 'Token eliminado correctamente'
                
                return Response({
                    'session_message': session_message,
                    'token_message': token_message
                }, status=status.HTTP_200_OK)
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado token en la solicitud'}, status=status.HTTP_409_CONFLICT)