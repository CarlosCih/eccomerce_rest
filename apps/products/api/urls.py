from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView
from apps.products.api.views.product_views import ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [
    # General endpoints
    path('measure-units/', MeasureUnitListAPIView.as_view(), name='measure-unit-list'),
    path('category-products/', CategoryProductListAPIView.as_view(), name='category-product-list'),
    path('indicators/', IndicatorListAPIView.as_view(), name='indicator-list'),
    
    # Products
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail-update-destroy'),
]