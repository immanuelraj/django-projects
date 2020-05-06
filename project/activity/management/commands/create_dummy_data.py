import random
import datetime
from django.contrib.auth import get_user_model
from activity.models import ActivityPeriod
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    first_names = ('John','Andy','Joe')
    last_names = ('Johnson','Smith','Williams')
    code = ('IN','US','NZ')
    tz = ('America/Los_Angeles', 'Asia/Kolkata', 'Europe/London')

    def create_random_user(self, count):
        data = {
            'username' : random.choice(self.first_names) + str(count),
            'password' : 'user' + str(count),
            'first_name' : random.choice(self.first_names),
            'last_name' : random.choice(self.last_names),
            'country' : random.choice(self.code),
            'tz' : random.choice(self.tz)
        }
        return User.objects.create_user(**data)

    def handle(self, *args, **kwargs):
        print('Creating dummy data')
        user = User.objects.get(username='admin')
        for count in range(1,251):
            data = {
                'user' : user,
                'start_time' : datetime.datetime.now(),
                'end_time' : datetime.datetime.now() + datetime.timedelta(days=1)
            }
            ActivityPeriod.objects.create(**data)
            if count % 10 == 0:
                user = self.create_random_user(count)
        print('Creation of dummy data is completed')