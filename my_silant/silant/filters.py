from .models import Car, Complaints, Maintenance
from django_filters import FilterSet

class CarFilter(FilterSet):
   class Meta:
       model = Car

       fields = {
            'technique_model__name': ['icontains'],
            'engine_model__name': ['icontains'],
            'transmission_model__name': ['icontains'],
            'drive_axle_model__name': ['icontains'],
            'steerable_axle_model__name': ['icontains']
            }
       
class CarFilterNoAut(FilterSet):
   class Meta:
       model = Car

       fields = {
           'serial_number': ['icontains']
           }
       
class MaintenanceFilter(FilterSet):
   class Meta:
       model = Maintenance

       fields = {
            'type_maintenance__name': ['icontains'],
            'service_company__name': ['icontains'],
            'car__serial_number': ['icontains'] #надо проверить, думаю не сработает
            }
       
class ComplaintsFilter(FilterSet):
   class Meta:
       model = Complaints

       fields = {
            'failure_node__name': ['icontains'],
            'recovery_method__name': ['icontains'],
            'service_company__name': ['icontains'] 
            }