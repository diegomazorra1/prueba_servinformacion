# Generated by Django 2.2.7 on 2019-11-09 17:49

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=11)),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('long_lat', django_google_maps.fields.GeoLocationField(max_length=100)),
                ('estadogeo', models.BooleanField(default=False)),
            ],
        ),
    ]
