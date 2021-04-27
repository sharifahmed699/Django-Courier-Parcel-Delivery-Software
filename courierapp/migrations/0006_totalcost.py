# Generated by Django 3.2 on 2021-04-26 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courierapp', '0005_alter_parcel_order_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Totalcost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcost', models.FloatField()),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courierapp.parcel')),
            ],
        ),
    ]
