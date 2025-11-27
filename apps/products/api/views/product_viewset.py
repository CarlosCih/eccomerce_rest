from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer
from rest_framework.response import Response

from rest_framework import generics, status, viewsets
from apps.users.authentication_mixins import Authentication

class ProductViewSet(Authentication, viewsets.ModelViewSet):
    
    """
    Docstring for ProductViewSet
    """
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk=None):
        """
        Un queryset es una colección de objetos de la base de datos que se pueden filtrar, ordenar y manipular de diversas maneras. En el contexto de Django REST Framework, un queryset se utiliza para definir qué datos estarán disponibles a través de una vista o un conjunto de vistas (viewset).
        """
        if pk is None:
            return self.serializer_class().Meta.model.objects.filter(state=True)
        else:
            return self.serializer_class().Meta.model.objects.filter(id=pk,state=True).first()

    def list(self, request):
        """
        Docstring for list
        
        :param self: Description
        :param request: Description
        """
        products = self.get_queryset()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """
        Docstring for create
        
        :param self: Description
        :param request: Description
        """
        # Sobrescribir el metodo create para personalizar la respuesta
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
        #end if
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """
        Docstring for retrieve
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        product = self.get_queryset(pk)
        if product:
            serializer = self.serializer_class(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        #end if
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        """
        Docstring for destroy
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        product = self.get_queryset(pk)
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_200_OK)
        #end if
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        """
        Docstring for update
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            #end if
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #end if
        
    def partial_update(self, request, pk=None):
        """
        Docstring for partial_update
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            #end if
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #end if