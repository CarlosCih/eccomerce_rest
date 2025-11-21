## Aqui se definen los serializdores para la app de usuarios
from rest_framework import serializers
from apps.users.models import User


# Esta serializador convierte el modelo User a un formato JSON y viceversa. 
# Es un serializador basico que incluye todos los campos del modelo User.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        