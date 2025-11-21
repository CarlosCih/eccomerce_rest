from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer
from apps.users.models import User
from rest_framework.response import Response

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
        return Response(users_serializer.data, status=200)
    elif request.method == 'POST':
        users_serializer = UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status=201)
        return Response(users_serializer.errors, status=418)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):

    if request.method == 'GET':
        user = User.objects.filter(id=pk).first()
        if user:
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=200)
    elif request.method == 'PUT':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=200)
        return Response(user_serializer.errors, status=418)
    elif request.method == 'DELETE':
        user = User.objects.filter(id=pk).first()
        if user:
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente!'}, status=200)
    return Response({'message': 'No se encontro un usuario con estos datos'}, status=404)

    