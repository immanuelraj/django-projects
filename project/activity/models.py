from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from timezone_field import TimeZoneField
from hotel import generate

class User(AbstractUser):

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
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


class ActivityPeriod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def check_unique(self, ext_id):
        return not ActivityPeriod.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
        super(ActivityPeriod, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']