from rest_framework import serializers
from django.contrib.auth.models import User

class TechniqueModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class EngineModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class TransmissionModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class DriveAxleModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class SteerableAxleModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "groups", "username"]

class ClientSerializer(serializers.Serializer):
    user = UserSerializer()
    name = serializers.CharField()
    description = serializers.CharField()

class ServiceCompanySerializer(serializers.Serializer):
    user = UserSerializer()
    name = serializers.CharField()
    description = serializers.CharField()

class CarSerializer(serializers.Serializer):
    serial_number = serializers.CharField() #Серийный номер
    technique_model = TechniqueModelSerializer() #Модель техники
    engine_model = EngineModelSerializer() #Модель двигателя
    engine_number = serializers.CharField() #Зав. № двигателя
    transmission_model = TransmissionModelSerializer() #Модель трансмиссии
    transmission_number = serializers.CharField() #Зав. № трансмиссии
    drive_axle_model = DriveAxleModelSerializer() #Модель ведущего моста
    drive_axle_number = serializers.CharField() #Зав. № ведущего моста
    steerable_axle_model = SteerableAxleModelSerializer #Модель управляемого моста
    steerable_axle_number = serializers.CharField() #Зав. № управляемого моста
    supply_contract = serializers.CharField() #Договор поставки №, дата
    shipping_date = serializers.DateField() #Дата отгрузки с завода
    consignee = serializers.CharField() #Грузополучатель (конечный потребитель)
    delivery_address = serializers.CharField() #Адрес поставки (эксплуатации)
    equipment = serializers.CharField() #Комплектация (доп. опции)
    client = ClientSerializer() #Клиент
    service_company = ServiceCompanySerializer() #Сервисная организация

class MiniCarSerializer(serializers.Serializer):
    serial_number = serializers.CharField() #Серийный номер
    technique_model = TechniqueModelSerializer() #Модель техники
    engine_model = EngineModelSerializer() #Модель двигателя
    engine_number = serializers.CharField() #Зав. № двигателя
    transmission_model = TransmissionModelSerializer() #Модель трансмиссии
    transmission_number = serializers.CharField() #Зав. № трансмиссии
    drive_axle_model = DriveAxleModelSerializer() #Модель ведущего моста
    drive_axle_number = serializers.CharField() #Зав. № ведущего моста
    steerable_axle_model = SteerableAxleModelSerializer #Модель управляемого моста
    steerable_axle_number = serializers.CharField() #Зав. № управляемого моста

class TypeMaintenanceSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class OrganizationMaintenanceSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class MaintenanceSerializer(serializers.Serializer):
    type_maintenance = OrganizationMaintenanceSerializer() #Вид ТО
    maintenance_date = serializers.DateField() #Дата проведения ТО
    operating_time = serializers.IntegerField() #Наработка м/час
    work_order = serializers.CharField() #№ заказа-наряда
    date_work_order = serializers.DateField() #Дата заказа-наряда
    organization_maintenance = OrganizationMaintenanceSerializer() #Организация, проводившая ТО
    car = CarSerializer() #Машина
    service_company = ServiceCompanySerializer() #Сервисная организация


class FailureNodeSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class RecoveryMethodSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class ComplaintsSerializer(serializers.Serializer):
    date_of_refusal = serializers.DateField() #Дата отказа
    operating_time = serializers.IntegerField() #Наработка м/час
    failure_node = FailureNodeSerializer #Узел отказа 
    description_failure = serializers.CharField() #Характер отказа
    recovery_method = RecoveryMethodSerializer() #Способ восстановления
    parts_used = serializers.CharField() #Используемые запасные части
    date_of_restoration = serializers.DateField() #Дата восстановления 
    equipment_downtime = serializers.IntegerField() #Время простоя техники
    car = CarSerializer() #Машина
    service_company = ServiceCompanySerializer() #Сервисная организация