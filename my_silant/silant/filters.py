from .models import Car, Complaints, Drive_axle_model, Engine_model, Failure_node, Maintenance, Recovery_method, Service_company, Steerable_axle_model, Technique_model, Transmission_model, Type_maintenance
from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from django import forms


class CarFilter(FilterSet):
    technique_model = ModelChoiceFilter(queryset=Technique_model.objects.all(), field_name='technique_model',label='Модель техники', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    engine_model = ModelChoiceFilter(queryset=Engine_model.objects.all(), field_name='engine_model',label='Модель двигателя', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    transmission_model = ModelChoiceFilter(queryset=Transmission_model.objects.all(), field_name='transmission_model',label='Модель трансмиссии', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    drive_axle_model = ModelChoiceFilter(queryset=Drive_axle_model.objects.all(), field_name='drive_axle_model',label='Модель ведущего моста', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    steerable_axle_model = ModelChoiceFilter(queryset=Steerable_axle_model.objects.all(), field_name='steerable_axle_model',label='Модель управляемого моста', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))     
    
    # class Meta:
    #     model = Car
    #     fields = {
    #         'technique_model', 'engine_model', 'transmission_model', 'drive_axle_model', 'steerable_axle_model'
    #         }

    #    fields = {
    #         'technique_model__name': ['icontains'],
    #         'engine_model__name': ['icontains'],
    #         'transmission_model__name': ['icontains'],
    #         'drive_axle_model__name': ['icontains'],
    #         'steerable_axle_model__name': ['icontains']
    #         }
       
class CarFilterNoAut(FilterSet):
    serial_number = CharFilter(field_name='serial_number',label='Серийный номер', lookup_expr='icontains', widget=forms.TextInput(attrs={"class":"form-control text-black text-center"}))
    class Meta:
        model = Car

        fields = {
            'serial_number'
            }
       
class MaintenanceFilter(FilterSet):
    type_maintenance = ModelChoiceFilter(queryset=Type_maintenance.objects.all(), field_name='type_maintenance',label='Вид ТО', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    service_company = ModelChoiceFilter(queryset=Service_company.objects.all(), field_name='service_company',label='Сервисная организация', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    car = ModelChoiceFilter(queryset=Car.objects.all(), field_name='car',label='Машина', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    # class Meta:
    #     model = Maintenance

    #     fields = {
    #         'type_maintenance__name', 'service_company__name', 'car__serial_number'
    #         }
       
class ComplaintsFilter(FilterSet):
    failure_node = ModelChoiceFilter(queryset=Failure_node.objects.all(), field_name='failure_node',label='Узел отказа', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    recovery_method = ModelChoiceFilter(queryset=Recovery_method.objects.all(), field_name='recovery_method',label='Способ восстановления', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    service_company = ModelChoiceFilter(queryset=Service_company.objects.all(), field_name='service_company',label='Сервисная организация', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))   
    car = ModelChoiceFilter(queryset=Car.objects.all(), field_name='car',label='Серийный номер Машины', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    # class Meta:
    #     model = Complaints

    #     fields = {
    #         'failure_node__name', 'recovery_method__name', 'service_company__name' 
    #         }