## Aqui se definen los serializdores para la app de usuarios
from rest_framework import serializers
from apps.users.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')
# Este serializador convierte el modelo User a un formato JSON y viceversa. 
# Es un serializador basico que incluye todos los campos del modelo User.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        update_user=super().update(instance,validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
class UserListSerializer(serializers.Serializer):
    class Meta:
        model = User
        
    def to_representation(self, instance):
        return {
            'ID': instance['id'],
            'Nombre_usuario': instance['username'],
            'Nombre': instance['name'],
            'Correo_electronico': instance['email'],
            'Contraseña': instance['password'],
        }
    
""" class TestSerializer(serializers.Serializer):
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
        return value
    
    def validate(self, data):
        return data
    
    #Metodo para crear una instancia de User a partir de los datos validados
    def create(self,validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save() # Guarda los cambios en la base de datos
        return instance
    
    def save(self):
        print(self) """