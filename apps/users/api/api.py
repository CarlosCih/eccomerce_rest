from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer, TestSerializer
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
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        test_data = {
            'username': 'ProsRumvan',
            'name': 'Rumvan',
            'email': 'Pros@example.com',
        }

        test_serializer = TestSerializer(data=test_data, context = test_data)

        if test_serializer.is_valid():
            user_instance = test_serializer.save()

            print("Usuario creado:" , user_instance) 
        else:
            print(test_serializer.errors)

        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        users_serializer = UserSerializer(data=request.data)
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
        if request.method == 'GET':
            if user:
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'PUT':
            user = User.objects.filter(id=pk).first()
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_418_IM_A_TEAPOT)
        
        elif request.method == 'DELETE':
            user = User.objects.filter(id=pk).first()
            if user:
                user.delete()
                return Response({'message': 'Usuario eliminado correctamente!'}, status=status.HTTP_200_OK)
            #end if
        #end elif
    #end if
    return Response({'message': 'No se encontro un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
#end def

    