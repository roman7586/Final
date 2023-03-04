from .models import Car
from django_filters import FilterSet

class CarFilter(FilterSet):
   class Meta:
       model = Car

       fields = {
           'technique_model__name': ['icontains']}