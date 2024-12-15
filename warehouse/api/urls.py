from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import ProductModelViewSet, ProductSupplyViewSet, UserModelViewSet, WarehouseModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('warehouses', WarehouseModelViewSet)
router.register('products', ProductModelViewSet)
router.register(r'product-supply', ProductSupplyViewSet,
                basename='product-supply')


urlpatterns = [
    # path('register/', register, name='register'),

]
urlpatterns.extend(router.urls)
