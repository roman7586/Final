from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'maintenance', MaintenanceViewSet)
router.register(r'complaints', ComplaintsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]