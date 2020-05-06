from django.contrib import admin
from django.contrib.auth import get_user_model
from activity.models import ActivityPeriod

User = get_user_model()


class ActivityPeriodAdmin(admin.ModelAdmin):
    search_fields = ('id', 'user__username',)
    list_display = [
        'id',
        'user',
        'start_time',
        'end_time',
    ]
    readonly_fields = ('ext_id',)
    autocomplete_fields = ['user']


class UserAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'user__username',)
    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'tz',
    ]
    readonly_fields = ('ext_id',)

admin.site.register(ActivityPeriod, ActivityPeriodAdmin)
admin.site.register(User, UserAdmin)