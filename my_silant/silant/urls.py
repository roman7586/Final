from django.urls import path

from .views import CarCreate, CarList


urlpatterns = [

    path('create/', CarCreate.as_view(), name='create_car'),
    path('', CarList.as_view())
]