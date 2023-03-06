from django.urls import path

from .views import CarCreate, CarEdit, CarList, viewdirectory


urlpatterns = [

    path('create/', CarCreate.as_view(), name='create_car'),
    path('edit/<int:pk>', CarEdit.as_view(), name='edit_car'),
    path('', CarList.as_view()),

    path('dictionary/<str:type>/<int:id>/', viewdirectory),
]