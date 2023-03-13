from django.urls import path

from .views import CarCreate, CarDetail, CarEdit, CarList, ComplaintsCreate, ComplaintsEdit, ComplaintsList, MaintenanceCreate, MaintenanceEdit, MaintenanceList, dictionaries, cardirectory, maintenancedirectory, complaintdirectory, savedictionary


urlpatterns = [

    path('', CarList.as_view()),
    path('<int:pk>', CarDetail.as_view(), name='car_info'),
    path('create/', CarCreate.as_view(), name='create_car'),
    path('edit/<int:pk>', CarEdit.as_view(), name='edit_car'),
    path('dictionaries/', dictionaries, name='dictionaries'),
    path('dictionary/<str:type>/<int:id>/', cardirectory),
    path('/maintenances/dictionary/<str:type>/<int:id>/', maintenancedirectory),
    path('dictionary/save/', savedictionary),

    path('maintenances/', MaintenanceList.as_view()), 
    path('maintenances/create/', MaintenanceCreate.as_view()),
    path('maintenances/edit/<int:pk>', MaintenanceEdit.as_view()),
    path('maintenances/dictionary/<str:type>/<int:id>/', maintenancedirectory),

    path('complaints/', ComplaintsList.as_view()), 
    path('complaints/create/', ComplaintsCreate.as_view()),
    path('complaints/edit/<int:pk>', ComplaintsEdit.as_view()), 
    path('complaints/dictionary/<str:type>/<int:id>/', complaintdirectory)
]