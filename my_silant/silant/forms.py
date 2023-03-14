
from django import forms
from .models import Car, Client, Complaints, Drive_axle_model, Engine_model, Maintenance, Organization_maintenance, Service_company, Steerable_axle_model, Technique_model, Transmission_model, Type_maintenance
from django.utils import timezone

now = timezone.now()

class CreateCarForm(forms.ModelForm):
    technique_model = forms.ModelChoiceField(queryset=Technique_model.objects.all(), label='Модель техники', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    engine_model = forms.ModelChoiceField(queryset=Engine_model.objects.all(), label='Модель двигателя', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    transmission_model = forms.ModelChoiceField(queryset=Transmission_model.objects.all(), label='Модель трансмиссии', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    drive_axle_model = forms.ModelChoiceField(queryset=Drive_axle_model.objects.all(), label='Модель ведущего моста', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    steerable_axle_model = forms.ModelChoiceField(queryset=Steerable_axle_model.objects.all(), label='Модель управляемого моста', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Клиент', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    service_company = forms.ModelChoiceField(queryset=Service_company.objects.all(), label='Сервисная организация', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))  
    class Meta:
        model = Car
        widgets = {'serial_number': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'engine_number': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'transmission_number': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'drive_axle_number': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'steerable_axle_number': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'supply_contract': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'consignee': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'delivery_address': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'equipment': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                    'shipping_date': forms.SelectDateWidget(years=list(reversed(range(2000, now.year+1))), attrs={"rows": 1,"class":"form-control text-black text-center"})  
                }
        fields = '__all__'


class CreateMaintenanceForm(forms.ModelForm):
    type_maintenance = forms.ModelChoiceField(queryset=Type_maintenance.objects.all(), label='Вид ТО', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    organization_maintenance = forms.ModelChoiceField (queryset=Organization_maintenance.objects.all(), label='Организация, проводившая ТО', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    car = forms.ModelChoiceField (queryset=Car.objects.all(), label='Машина', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    service_company = forms.ModelChoiceField (queryset=Service_company.objects.all(), label='Сервисная организация', widget=forms.Select(attrs={"class":"form-control text-black text-center"}))
    operating_time = forms.IntegerField (min_value='0', label='Наработка м/час', widget=forms.NumberInput (attrs={"class":"form-control text-black text-center"}))
    class Meta:
        model = Maintenance
        widgets = {'maintenance_date': forms.SelectDateWidget(years=list(reversed(range(2000, now.year+1))), attrs={"rows": 1,"class":"form-control text-black text-center"}),
                   'work_order': forms.Textarea(attrs={"rows": 1,"class":"form-control text-black text-center"}),
                   'date_work_order': forms.SelectDateWidget(years=list(reversed(range(2000, now.year+1))), attrs={"rows": 1,"class":"form-control text-black text-center"}),
        }
        fields = '__all__'

class CreateComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        widgets = {'date_of_refusal': forms.SelectDateWidget(years=list(reversed(range(2000, now.year+1)))),
                   'description_failure': forms.Textarea(attrs={'rows': 1}),
                   'parts_used': forms.Textarea(attrs={'rows': 1}),
                   'date_of_restoration': forms.SelectDateWidget(years=list(reversed(range(2000, now.year+1))))

        }
        fields = '__all__'