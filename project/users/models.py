from django.db import models
from hotel import generate
from timezone_field import TimeZoneField
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    phone = PhoneNumberField(null=False, blank=False)
    country = CountryField(multiple=False, blank=True, null=True)
    tz = TimeZoneField()
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def check_unique(self, ext_id):
        User = get_user_model()
        return not User.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']