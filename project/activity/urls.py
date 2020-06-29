from django.urls import path
from . import views

app_name = 'activity'

urlpatterns = [
    path('user-activity/', views.UserActivityListViewSet.as_view()),
]