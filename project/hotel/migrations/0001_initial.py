# Generated by Django 2.2 on 2020-04-02 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('city_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country_name', models.CharField(blank=True, max_length=50, null=True)),
                ('property_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Hotel', 'Hotel'), ('ApartHotel', 'ApartHotel')], max_length=10)),
                ('contact_person', models.CharField(blank=True, max_length=150, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=40, null=True)),
                ('ext_id', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('Studio', 'STUDIO'), ('1 BR', '1 BR'), ('2 BR', '2 BR'), ('3 BR', '3 BR')], max_length=10)),
                ('display_name', models.CharField(blank=True, max_length=150, null=True)),
                ('max_occupancy', models.PositiveIntegerField(default=1)),
                ('room_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('tv_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('wifi_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('bearkfast_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('couch_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('table_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('ac_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('total_room_price', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('ext_id', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
