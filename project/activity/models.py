from django.db import models
from hotel import generate
from django.conf import settings



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