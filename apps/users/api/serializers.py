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
    username = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    #Validacion personalizada
    def validate_name(self, value):
        if 'John' in value:
            raise serializers.ValidationError("El nombre no puede contener 'John'", code='invalid_name')
        
        print(self.context)

        return value
    
    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError("El email no puede estar vacio", code='empty_email')
        
        if self.context['name'] in value:
            raise serializers.ValidationError("El email no puede contener el nombre", code='email_contains_name')
        return value
    
    def validate(self, data):
        return data
    
    def create(self,validated_data):
        return User.objects.create(**validated_data)