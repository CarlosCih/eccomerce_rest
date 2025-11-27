from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta, datetime
from django.utils import timezone
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):
    
    """Custom token authentication class that can be extended for token expiration logic."""
    
    
    # Metodo para calcular el tiempo restante antes de que el token expire
    def expires_in(self, token):
        
        # Calcular el tiempo transcurrido desde la creacion del token
        time_elapsed = timezone.now() - token.created
        
        # Calcular el tiempo restante antes de la expiracion del token
        left_time = timedelta(seconds= settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        
        return left_time
    
    # Metodo para verificar si el token ha expirado
    def is_token_expired(self, token):
        
        # Verifica si el tiempo restante es menor que cero
        return self.expires_in(token) < timedelta(seconds=0)
    
    # Metodo para manejar la expiracion del token
    def token_expired_handler(self, token):
        
        # Verifica si el token ha expirado
        is_expired = self.is_token_expired(token)
        
        # Si el token ha expirado, imprime un mensaje en la consola
        if is_expired:
            
            print("Token expired")
            
        return is_expired
    
    # Here you can add methods to handle token expiration if needed.
    def authenticate_credentials(self, key):
        
        # Override to add custom behavior for token authentication
        try:
            # Obtiene el token con el usuario relacionado
            token = self.get_model().objects.select_related('user').get(key=key)
            
        # Captura la excepción si el token no existe
        except self.get_model().DoesNotExist:
            
            # Lanza una excepción de autenticación si el token no es válido
            message = 'Invalid token. Please log in again.'
            return message
        
        # Si el usuario asociado al token no está activo, lanza una excepción
        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted.')
        
        """Verifica si el token ha expirado y maneja la expiración"""
        is_expired = self.token_expired_handler(token)
        
        # Si el token ha expirado, lanza una excepcion de autenticacion
        if is_expired:
            print("Token has expired.")
            raise AuthenticationFailed('Token has expired.')
        
        return (token.user, token)