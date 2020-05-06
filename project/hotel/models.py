from datetime import datetime
from django.apps import apps
from django.db import models
from django.conf import settings
from hotel import generate


class Hotel(models.Model):
    TYPES = (
        ('Apartment', 'Apartment'),
        ('Hotel', 'Hotel'),
        ('ApartHotel', 'ApartHotel'),
    )
    name = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    city_name = models.CharField(max_length=50, null=True, blank=True)
    country_name = models.CharField(max_length=50, null=True, blank=True)
    property_type = models.CharField(max_length=10, choices=TYPES)
    contact_person = models.CharField(max_length=150, null=True, blank=True)
    contact_phone = models.CharField(max_length=40, null=True, blank=True)
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def check_unique(self, ext_id):
        return not Hotel.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
        super(Hotel, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

class Room(models.Model):

    TYPES = (('Studio', 'STUDIO'), ('1 BR', '1 BR'), ('2 BR', '2 BR'), ('3 BR', '3 BR'))
    room_type = models.CharField(max_length=10, choices=TYPES)
    display_name = models.CharField(max_length=150, null=True, blank=True)
    max_occupancy = models.PositiveIntegerField(default=1)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    tv_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    wifi_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    bearkfast_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    couch_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    table_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    ac_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    total_room_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    ext_id = models.CharField(max_length=15, null=True, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def check_unique(self, ext_id):
        return not Room.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
        self.total_room_price = sum([self.room_price, self.wifi_price, self.bearkfast_price, self.tv_price, self.couch_price, self.table_price, self.ac_price])
        super(Room, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']