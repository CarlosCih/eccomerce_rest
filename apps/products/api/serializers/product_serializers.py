from apps.products.models import Product
from rest_framework import serializers

from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer

class ProductSerializer(serializers.ModelSerializer):
    """Metodos para serializar los productos"""
    
    #Primer metodo: ModelSerializer
    """ measure_unit = MeasureUnitSerializer()
    category_product = CategoryProductSerializer() """
    """En este caso no es necesario el IndicatorSerializer porque no hay relacion directa, pero los nombres deben ser lo mismos que en el modelo"""

    #Segundo metodo: Meta class
    """measure_unit = serializers.StringRelatedField()
    category_product = serializers.StringRelatedField()"""
    """En este caso no es necesario el IndicatorSerializer porque no hay relacion directa, pero los nombres deben ser lo mismos que en el modelo en el metodo __Str__"""
    
    #Tercer metodo: to_representation
    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','delete_date',)
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image else None,
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description,
        }