
from silant.models import Car, Maintenance, Complaints
from rest_framework import viewsets
from .serializers import CarSerializer, MaintenanceSerializer, ComplaintsSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('shipping_date')
    serializer_class = CarSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all().order_by('maintenance_date')
    serializer_class = MaintenanceSerializer

class ComplaintsViewSet(viewsets.ModelViewSet):
    queryset = Complaints.objects.all().order_by('date_of_refusal')
    serializer_class = ComplaintsSerializer
