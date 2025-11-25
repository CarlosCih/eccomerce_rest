from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """BaseModel Model Definition."""

    #TODO: Definir los campos comunes para los demas modelos
    id = models.AutoField(primary_key=True)
    state = models.BooleanField("Estado", default=True)
    created_date = models.DateTimeField("Fecha de creacion", auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField("Fecha de modificacion", auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)
    

    class Meta:
        """Meta definition for BaseModel."""
        abstract= True # Indica que es una clase abstracta y no se creara una tabla en la base de datos
        verbose_name = "Modelo Base"
        verbose_name_plural = "Modelos Base"