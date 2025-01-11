from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import ProductModelViewSet, StockViewSet, TransactionCreateView, UserModelViewSet, UserRegistrationViewSet, WarehouseModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('warehouses', WarehouseModelViewSet)
router.register('products', ProductModelViewSet)
router.register('transaction', TransactionCreateView)
router.register('stock', StockViewSet)


urlpatterns = [
    path('register/',
         UserRegistrationViewSet.as_view({'post': 'create'}), name='user-register'),


]
urlpatterns.extend(router.urls)
