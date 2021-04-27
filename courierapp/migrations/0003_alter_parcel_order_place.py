# Generated by Django 3.2 on 2021-04-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courierapp', '0002_alter_parcel_order_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='order_place',
            field=models.CharField(choices=[('ID', 'Inside of Dhaka'), ('DD', 'Division of Dhaka'), ('OD', 'Outside of Dhaka')], max_length=50),
        ),
    ]