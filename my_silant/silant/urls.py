from django.urls import path

from .views import CarCreate, CarEdit, CarList, dictionaries, viewdirectory


urlpatterns = [

    path('', CarList.as_view()),
    path('create/', CarCreate.as_view(), name='create_car'),
    path('edit/<int:pk>', CarEdit.as_view(), name='edit_car'),
    path ('dictionaries/', dictionaries, name='dictionaries'),

    path('dictionary/<str:type>/<int:id>/', viewdirectory),
]