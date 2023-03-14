
from silant.models import Car, Maintenance, Complaints
from rest_framework import viewsets, permissions
from .serializers import CarSerializer, MaintenanceSerializer, ComplaintsSerializer, MiniCarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('shipping_date')
    serializer_class = CarSerializer
    def get_serializer_class(self):
        if not self.request.user.is_authenticated:
            return MiniCarSerializer # если не авторизован отобразить краткий список
        else:
            return CarSerializer # если не авторизован отобразить полный список

# Для настройки видимости полей с использованием API в views.py в зависимости от прав, следует использовать декораторы доступа к представлениям (permissions). Эти декораторы позволяют задавать различные права доступа к представлениям в вашем API на основе аутентификации и авторизации пользователей.

# Пример:

# from rest_framework import permissions

# class MyViewSet(viewsets.ModelViewSet):
#     queryset = MyModel.objects.all()
#     serializer_class = MySerializer

#     permission_classes = [permissions.IsAuthenticated]

#     def get_serializer_class(self):


#         """Override serializer for fields visibility based on user permission.""" 
#           Переопределить сериализатор для видимости полей на основе разрешения пользователя


#         if not self.request.user.is_authenticated:
#             return AnonymousSerializer

#         # get the serializer based on the user permission
#           получить сериализатор на основе разрешения пользователя

#         if self.request.user.has_perm('myapp.view_all_fields'):
#             return AllFieldsSerializer
#         else:
#             return FilteredFieldsSerializer

# В этом примере мы использовали декораторы доступа к представлениям, чтобы указать, что доступ к представлению должен быть только для аутентифицированных пользователей (permissions.IsAuthenticated).
# Далее мы определили метод get_serializer_class () для определения сериализатора в зависимости от прав доступа пользователя. То есть, если пользователь имеет разрешение 'myapp.view_all_fields', мы используем сериализатор AllFieldsSerializer, который показывает все поля модели. В противном случае мы используем сериализатор FilteredFieldsSerializer, который показывает только определенные поля модели, доступные для этого пользователя.
# Это далеко не единственный способ конфигурации видимости полей с использованием API в views.py, но он является довольно распространенным и эффективным.

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all().order_by('maintenance_date')
    serializer_class = MaintenanceSerializer
    permission_classes = [permissions.IsAuthenticated] # Отображение значений только авторизованным

class ComplaintsViewSet(viewsets.ModelViewSet):
    queryset = Complaints.objects.all().order_by('date_of_refusal')
    serializer_class = ComplaintsSerializer
    permission_classes = [permissions.IsAuthenticated] # Отображение значений только авторизованным
    
