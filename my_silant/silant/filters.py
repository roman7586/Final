from .models import Car, Complaints, Maintenance, Technique_model
from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from django import forms


class CarFilter(FilterSet):
    technique_model = ModelChoiceFilter(queryset=Technique_model.objects.all(), field_name='technique_model',label='Модель техники', widget=forms.Select(attrs={"class":"form-control text-black text-center","max_length":"100"}))     
    serial_number = CharFilter(field_name='serial_number',label='Серийный номер', lookup_expr='icontains', widget=forms.TextInput(attrs={"class":"form-control text-black text-center","max_length":"100"}))

    class Meta:
         model = Car
         fields = {
             'serial_number', 'technique_model'
             }

    #    fields = {
    #         'technique_model__name': ['icontains'],
    #         'engine_model__name': ['icontains'],
    #         'transmission_model__name': ['icontains'],
    #         'drive_axle_model__name': ['icontains'],
    #         'steerable_axle_model__name': ['icontains']
    #         }
       
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
            'car__serial_number': ['icontains'] 
            }
       
class ComplaintsFilter(FilterSet):
   class Meta:
       model = Complaints

       fields = {
            'failure_node__name': ['icontains'],
            'recovery_method__name': ['icontains'],
            'service_company__name': ['icontains'] 
            }