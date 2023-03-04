from django.db import models
from django.contrib.auth.models import User

class Base_dictionary(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        abstract = True
        
    def __str__(self):
        return f'{self.name}'
    
# Create your models here.
class Technique_model(Base_dictionary):

    class Meta:
        verbose_name = 'Модель техники'


class Engine_model(Base_dictionary):

    class Meta:
        verbose_name = 'Модель двигателя'


class Transmission_model(Base_dictionary):

    class Meta:
        verbose_name = 'Модель трансмиссии'


class Drive_axle_model(Base_dictionary):

    class Meta:
        verbose_name = 'Модель ведущего моста'


class Steerable_axle_model(Base_dictionary):

    class Meta:
        verbose_name = 'Модель управляемого моста'


class Service_company(Base_dictionary):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')

    class Meta:
        verbose_name = 'Сервисные компании'


class Car(models.Model):
    serial_number = models.TextField(max_length=30, unique=True, db_index=True, verbose_name='Зав. № машины')
    technique_model = models.ForeignKey(Technique_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель техники')
    engine_model = models.ForeignKey(Engine_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель двигателя')
    engine_number = models.TextField(max_length=30, verbose_name='Зав. № двигателя')
    transmission_model = models.ForeignKey(Transmission_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель трансмиссии')
    transmission_number = models.TextField(max_length=50, verbose_name='Зав. № трансмиссии')
    drive_axle_model = models.ForeignKey(Drive_axle_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель ведущего моста')
    drive_axle_number = models.TextField(max_length=50, verbose_name='Зав. № ведущего моста')
    steerable_axle_model = models.ForeignKey(Steerable_axle_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель управляемого моста')
    steerable_axle_number = models.TextField(max_length=50, verbose_name='Зав. № управляемого моста')
    supply_contract = models.TextField(max_length=50, blank=True, verbose_name='Договор поставки №, дата.')
    shipping_date = models.DateField(db_index=True, verbose_name='Дата отгрузки с завода')
    consignee = models.TextField(max_length=50, blank=True, verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.TextField(max_length=150, blank=True, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(max_length=150, blank=True, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Клиент')
    service_company = models.ForeignKey(Service_company, null=True, on_delete=models.CASCADE, blank=True, verbose_name='Сервисная организация')

    def __str__(self):
        return f'{self.serial_number}'

    class Meta:
        verbose_name = 'Машины'
        ordering = ['shipping_date']


class Type_maintenance(Base_dictionary):

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Вид ТО'


class Organization_maintenance(Base_dictionary):
  
        class Meta:
            verbose_name = 'Организация, проводившая ТО'

class Maintenance(models.Model):
    type_maintenance = models.ForeignKey(Type_maintenance, on_delete=models.CASCADE, verbose_name='Вид ТО')
    maintenance_date = models.DateField(verbose_name='Дата проведения ТО')
    operating_time = models.IntegerField(verbose_name='Наработка м/час')
    work_order = models.TextField(max_length=50, verbose_name='№ заказа-наряда')
    date_work_order = models.DateField(verbose_name='Дата заказа-наряда')
    organization_maintenance = models.ForeignKey(Organization_maintenance, on_delete=models.CASCADE, verbose_name='Организация, проводившая ТО')
    car = models.OneToOneField(Car, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.OneToOneField(Service_company, on_delete=models.CASCADE,verbose_name='Сервисная организация')

    def __str__(self):
        return f'{self.car}'

    class Meta:
        verbose_name = 'ТО'
        ordering = ['maintenance_date']



class Failure_node(Base_dictionary):

    class Meta:
        verbose_name = 'Узел отказа'


class Recovery_method(Base_dictionary):

    class Meta:
        verbose_name = 'Способ восстановления'


class Complaints(models.Model):
    date_of_refusal = models.DateField(verbose_name='Дата отказа')
    operating_time = models.IntegerField(verbose_name='Наработка м/час')
    failure_node = models.ForeignKey(Failure_node, on_delete=models.CASCADE, verbose_name='Узел отказа') 
    description_failure = models.TextField(max_length=1024, verbose_name='Характер отказа')
    recovery_method = models.ForeignKey(Recovery_method, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    parts_used = models.TextField(verbose_name='Используемые запасные части')
    date_of_restoration = models.DateField(verbose_name='Дата восстановления') 
    equipment_downtime = models.IntegerField(verbose_name='Время простоя техники')
    car = models.OneToOneField(Car, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.OneToOneField(Service_company, on_delete=models.CASCADE, verbose_name='Сервисная организация')

    def __str__(self):
        return f'{self.car}'

    class Meta:
        verbose_name = 'Рекламации'
        ordering = ['date_of_refusal']

