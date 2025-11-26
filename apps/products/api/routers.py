from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_viewset import ProductViewSet
from apps.products.api.views.general_views import *

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')
router.register(r'measure-unit', MeasureUnitViewSet, basename='measureunit')
router.register(r'indicators', IndicatorViewSet, basename='indicator')
router.register(r'category-products', CategoryProductViewSet, basename='categoryproduct')

urlpatterns = router.urls

