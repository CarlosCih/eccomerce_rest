## Aqui se definen los serializdores para la app de usuarios
from rest_framework import serializers
from apps.users.models import User


# Esta serializador convierte el modelo User a un formato JSON y viceversa. 
# Es un serializador basico que incluye todos los campos del modelo User.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    age = serializers.IntegerField()

    #Validacion personalizada
    def validate_name(self, value):
        print(value)
        return value
    
    def validate_email(self, value):
        print(value)
        return value
    
    def validate_age(self, value):
        print(value)
        return value
    
    def validate(self, data):
        print('Validating entire data:', data)
        return data