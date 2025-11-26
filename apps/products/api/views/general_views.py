
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer
from apps.base.api import GeneralListAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response


class MeasureUnitViewSet(viewsets.GenericViewSet):
    """
    Docstring for MeasureUnitViewSet
    """
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self, pk=None):
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
        data = self.get_queryset()
        data = self.serializer_class(data, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    
    
    def create(self, request):
        """
        Docstring for create
        
        :param self: Description
        :param request: Description
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Measure Unit created successfully'}, status=status.HTTP_201_CREATED)
        #end if
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self, request, pk=None):
        """
        Docstring for retrieve
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        measure_unit = self.get_queryset(pk)
        if measure_unit:
            serializer = self.serializer_class(measure_unit)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        #end if
        return Response({'error': 'Measure Unit not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def destroy(self, request, pk=None):
        """
        Docstring for destroy
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        measure_unit = self.get_queryset(pk)
        if measure_unit:
            measure_unit.state = False
            measure_unit.save()
            return Response({'message': 'Measure Unit deleted successfully'}, status=status.HTTP_200_OK)
        #end if
        return Response({'error': 'Measure Unit not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def update(self, request, pk=None):
        """
        Docstring for update
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        if self.get_queryset(pk):
            measure_unit_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if measure_unit_serializer.is_valid():
                measure_unit_serializer.save()
                return Response(measure_unit_serializer.data, status=status.HTTP_200_OK)
            #end if
            return Response(measure_unit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #end if
    
    
    def partial_update(self, request, pk=None):
        """
        Docstring for partial_update
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        if self.get_queryset(pk):
            measure_unit_serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if measure_unit_serializer.is_valid():
                measure_unit_serializer.save()
                return Response(measure_unit_serializer.data, status=status.HTTP_200_OK)
            #end if
            return Response(measure_unit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #end if
    
class CategoryProductViewSet(viewsets.GenericViewSet):
    """
    Docstring for CategoryProductViewSet
    """
    serializer_class = CategoryProductSerializer
    
    def get_queryset(self, pk=None):
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
        data = self.get_queryset()
        data = self.serializer_class(data, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    def create(self, request):
        """
        Docstring for create
        
        :param self: Description
        :param request: Description
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category Product created successfully'}, status=status.HTTP_201_CREATED)
        #end if
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self, request, pk=None):
        """
        Docstring for retrieve
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        category_product = self.get_queryset(pk)
        if category_product:
            serializer = self.serializer_class(category_product)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        #end if
        return Response({'error': 'Category Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def destroy(self, request, pk=None):
        """
        Docstring for destroy
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        category_product = self.get_queryset(pk)
        if category_product:
            category_product.state = False
            category_product.save()
            return Response({'message': 'Category Product deleted successfully'}, status=status.HTTP_200_OK)
        #end if
        return Response({'error': 'Category Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def update(self, request, pk=None):
        """
        Docstring for update
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        if self.get_queryset(pk):
            category_product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if category_product_serializer.is_valid():
                category_product_serializer.save()
                return Response(category_product_serializer.data, status=status.HTTP_200_OK)
            #end if
            return Response(category_product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #end if
        
    def partial_update(self, request, pk=None):
        """
        Docstring for partial_update
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        if self.get_queryset(pk):
            category_product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if category_product_serializer.is_valid():
                category_product_serializer.save()
                return Response(category_product_serializer.data, status=status.HTTP_200_OK)
            #end if
            return Response(category_product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #end if    
class IndicatorViewSet(viewsets.GenericViewSet):
    """
    Docstring for IndicatorViewSet
    """
    serializer_class = IndicatorSerializer
    
    def get_queryset(self, pk=None):
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
        data = self.get_queryset()
        data = self.serializer_class(data, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    
    
    def create(self, request):
        """
        Docstring for create
        
        :param self: Description
        :param request: Description
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Indicator created successfully'}, status=status.HTTP_201_CREATED)
        #end if
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self, request, pk=None):
        """
        Docstring for retrieve
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        indicator = self.get_queryset(pk)
        if indicator:
            serializer = self.serializer_class(indicator)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        #end if
        return Response({'error': 'Indicator not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def destroy(self, request, pk=None):
        """
        Docstring for destroy
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        indicator = self.get_queryset(pk)
        if indicator:
            indicator.state = False
            indicator.save()
            return Response({'message': 'Indicator deleted successfully'}, status=status.HTTP_200_OK)
        #end if
        return Response({'error': 'Indicator not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def update(self, request, pk=None):
        """
        Docstring for update
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        if self.get_queryset(pk):
            indicator_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if indicator_serializer.is_valid():
                indicator_serializer.save()
                return Response(indicator_serializer.data, status=status.HTTP_200_OK)
            #end if
            return Response(indicator_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #end if
        
    def partial_update(self, request, pk=None):
        """
        Docstring for partial_update
        
        :param self: Description
        :param request: Description
        :param pk: Description
        """
        if self.get_queryset(pk):
            indicator_serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if indicator_serializer.is_valid():
                indicator_serializer.save()
                return Response(indicator_serializer.data, status=status.HTTP_200_OK)
            #end if
            return Response(indicator_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #end if
