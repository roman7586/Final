
from django import forms
from .models import Car, Maintenance
from django.utils import timezone

now = timezone.now()

class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        widgets = {'serial_number': forms.Textarea(attrs={'rows': 1}),
                   'engine_number': forms.Textarea(attrs={'rows': 1}),
                   'transmission_number': forms.Textarea(attrs={'rows': 1}),
                   'drive_axle_number': forms.Textarea(attrs={'rows': 1}),
                   'steerable_axle_number': forms.Textarea(attrs={'rows': 1}),
                   'supply_contract': forms.Textarea(attrs={'rows': 1}),
                   'consignee': forms.Textarea(attrs={'rows': 1}),
                   'delivery_address': forms.Textarea(attrs={'rows': 1}),
                   'equipment': forms.Textarea(attrs={'rows': 1}),
                   'shipping_date': forms.SelectDateWidget(years=list(reversed(range(2000, now.year+1)))) }
        fields = '__all__'

#class Directory(forms.Form):
#    name = forms.CharField(label='name', max_length=20)
#    description = forms.CharField(label='name', max_length=100)

class CreateMaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        widgets = {'maintenance_date': forms.SelectDateWidget(years=list(reversed(range(2000, now.year+1)))),
                   'work_order': forms.Textarea(attrs={'rows': 1}),
                   'date_work_order': forms.SelectDateWidget(years=list(reversed(range(2000, now.year+1)))),
        }
        fields = '__all__'