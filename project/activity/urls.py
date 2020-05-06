from django.urls import path, include
from .views import UserActivityListViewSet

app_name = 'activity'

urlpatterns = [
    path('user-activity/', UserActivityListViewSet.as_view()),
]