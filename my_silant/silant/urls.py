from django.urls import path

from .views import CarCreate, CarList, createdirectory


urlpatterns = [

    path('create/', CarCreate.as_view(), name='create_car'),
    path('', CarList.as_view()),

    path('dictionary/<str:type>/<int:id>/', createdirectory),
]