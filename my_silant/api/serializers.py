from silant.models import Car, Maintenance, Complaints, Technique_model
from rest_framework import serializers

class TechniqueModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    # engine_model = models.ForeignKey(Engine_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель двигателя')
    # engine_number = models.TextField(max_length=30, verbose_name='Зав. № двигателя')
    # transmission_model = models.ForeignKey(Transmission_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель трансмиссии')
    # transmission_number = models.TextField(max_length=50, verbose_name='Зав. № трансмиссии')
    # drive_axle_model = models.ForeignKey(Drive_axle_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель ведущего моста')
    # drive_axle_number = models.TextField(max_length=50, verbose_name='Зав. № ведущего моста')
    # steerable_axle_model = models.ForeignKey(Steerable_axle_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель управляемого моста')
    # steerable_axle_number = models.TextField(max_length=50, verbose_name='Зав. № управляемого моста')
    # supply_contract = models.TextField(max_length=50, blank=True, verbose_name='Договор поставки №, дата.')
    # shipping_date = models.DateField(db_index=True, verbose_name='Дата отгрузки с завода')
    # consignee = models.TextField(max_length=50, blank=True, verbose_name='Грузополучатель (конечный потребитель)')
    # delivery_address = models.TextField(max_length=150, blank=True, verbose_name='Адрес поставки (эксплуатации)')
    # equipment = models.TextField(max_length=150, blank=True, verbose_name='Комплектация (доп. опции)')
    # client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Клиент')
    # service_company = models.ForeignKey(Service_company, on_delete=models.CASCADE, blank=True, verbose_name='Сервисная организация')


class CarSerializer(serializers.Serializer):
    serial_number = serializers.CharField()
    technique_model = TechniqueModelSerializer() #models.ForeignKey(Technique_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель техники')



# class CarSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Car
#         fields = ('serial_number', 'shipping_date', 'technique_model') #'__all__'

# class Technique_modelSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Technique_model
#         fields = '__all__'

# class MaintenanceSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Maintenance
#         fields = '__all__'

# class ComplaintsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Complaints
#         fields = '__all__'