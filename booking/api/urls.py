from rest_framework.routers import DefaultRouter

from api.views import BookingModelViewSet, HotelModelViewSet, RoomModelViewSet, UserModelViewSet

router=DefaultRouter()
router.register('users',UserModelViewSet)
router.register('hotels',HotelModelViewSet)
router.register('rooms',RoomModelViewSet)
router.register('bookings',BookingModelViewSet)

urlpatterns = [
    
]

urlpatterns.extend(router.urls)
