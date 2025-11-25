from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer,UserListSerializer
from apps.users.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



""" class UserApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=200) """

@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'name', 'email', 'password')
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    #create user
    elif request.method == 'POST':
        users_serializer = UserSerializer(data=request.data)
        #validate data
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({'message': 'Usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        #end if
        return Response(users_serializer.errors, status=status.HTTP_418_IM_A_TEAPOT)
    #end elif
    return Response({'message': 'Metodo no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#end def
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    user = User.objects.filter(id=pk).first()

    if user:
        #get user
        if request.method == 'GET':
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        #update user    
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_418_IM_A_TEAPOT)
        
        #delete user
        elif request.method == 'DELETE':
                user.delete()
                return Response({'message': 'Usuario eliminado correctamente!'}, status=status.HTTP_200_OK)
            #end if
        #end elif
    #end if
    return Response({'message': 'No se encontro un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
#end def

    