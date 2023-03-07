from django.urls import path

from .views import CarCreate, CarEdit, CarList, ComplaintsCreate, ComplaintsEdit, ComplaintsList, MaintenanceCreate, MaintenanceEdit, MaintenanceList, dictionaries, viewdirectory


urlpatterns = [

    path('', CarList.as_view()),
    path('create/', CarCreate.as_view(), name='create_car'),
    path('edit/<int:pk>', CarEdit.as_view(), name='edit_car'),
    path('dictionaries/', dictionaries, name='dictionaries'),
    path('dictionary/<str:type>/<int:id>/', viewdirectory),

    path('maintenances/', MaintenanceList.as_view()), 
    path('maintenances/create/', MaintenanceCreate.as_view()),
    path('maintenances/edit/<int:pk>', MaintenanceEdit.as_view()), 

    path('сomplaints/', ComplaintsList.as_view()), 
    path('сomplaints/create/', ComplaintsCreate.as_view()),
    path('сomplaints/edit/<int:pk>', ComplaintsEdit.as_view()), 
]