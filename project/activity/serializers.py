from rest_framework import serializers
from django.contrib.auth import get_user_model
from activity.models import ActivityPeriod

User = get_user_model()


class ActivityPeriodSerializer(serializers.Serializer):

    start_time = serializers.DateTimeField(format="%b %d %Y %I:%M %p")
    end_time = serializers.DateTimeField(format="%b %d %Y %I:%M %p")

    def get_start_time(self, obj):
        return obj.start_time

    def get_end_time(self, obj):
        return obj.start_time

    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class UserListSerializer(serializers.Serializer):

    id = serializers.SerializerMethodField()
    real_name = serializers.SerializerMethodField()
    tz = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.ext_id

    def get_real_name(self, obj):
        return '{0} {1}'.format(obj.first_name, obj.last_name)

    def get_tz(self, obj):
        return str(obj.tz)

    def get_activity_periods(self, obj):
        if ActivityPeriod.objects.filter(user=obj).exists():
            return ActivityPeriodSerializer(ActivityPeriod.objects.filter(user=obj), many=True).data

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']