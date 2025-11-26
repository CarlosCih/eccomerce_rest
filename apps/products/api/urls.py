from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView
from eccomerce_rest.apps.products.api.views.product_viewset import ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [
    # General endpoints
    path('measure-units/', MeasureUnitListAPIView.as_view(), name='measure-unit-list'),
    path('category-products/', CategoryProductListAPIView.as_view(), name='category-product-list'),
    path('indicators/', IndicatorListAPIView.as_view(), name='indicator-list'),
]