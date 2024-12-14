from rest_framework.routers import DefaultRouter

from api.views import ProductModelViewSet, UserModelViewSet, WarehouseModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('warehouses', WarehouseModelViewSet)
router.register('products', ProductModelViewSet)

urlpatterns = [

]
urlpatterns.extend(router.urls)
