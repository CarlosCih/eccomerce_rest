from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView

urlpatterns = [
    path('measure-units/', MeasureUnitListAPIView.as_view(), name='measure-unit-list'),
    path('category-products/', CategoryProductListAPIView.as_view(), name='category-product-list'),
    path('indicators/', IndicatorListAPIView.as_view(), name='indicator-list'),
]