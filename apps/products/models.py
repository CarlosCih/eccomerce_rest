from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):
    """Model definition for MeasureUnit."""
    
    #TODO: Define fields here
    description = models.CharField('Descripcion', max_length=50,blank= False,null=False,unique=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class Meta:
        """Meta definition for MeasureUnit."""
        
        db_table = ''
        managed = True
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'
        
    def __str__(self):
        return self.description
class CategoryProduct(BaseModel):
    """Model definition for CategoryProduct."""
    description = models.CharField('Descripcion', max_length=50,blank= False,null=False,unique=True)
    
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for CategoryProduct."""
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Producto'
        
    def __str__(self):
        return self.description
    
class Indicator(BaseModel):
    #TODO: Define fields here
    descount = models.PositiveIntegerField(default=0)
    category_product = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Oferta'
        
    def __str__(self):
        return f'Oferta de {self.descount} % para la categoria {self.category_product.description}'
    
class Product(BaseModel):
    """Model definition for Product."""
    name = models.CharField('Nombre del Producto', max_length=150, blank=False, null=False, unique=True)
    description = models.TextField('Descripcion del Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', max_length=255, null=True, blank = True)
    measure_unit  = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True, blank=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria del Producto', null=True, blank=True)

    
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return self.name