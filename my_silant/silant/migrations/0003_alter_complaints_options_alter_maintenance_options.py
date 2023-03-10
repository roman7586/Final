# Generated by Django 4.0.5 on 2023-03-12 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('silant', '0002_alter_maintenance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaints',
            options={'ordering': ['date_of_refusal'], 'permissions': (('view_complaints_noclient', 'complaints view no client'),), 'verbose_name': 'Рекламации', 'verbose_name_plural': 'Рекламации'},
        ),
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['maintenance_date'], 'permissions': (('view_maintenance_noclient', 'maintenance view no client'),), 'verbose_name': 'ТО', 'verbose_name_plural': 'ТО'},
        ),
    ]
