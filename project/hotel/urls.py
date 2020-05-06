from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'hotel'

urlpatterns = [
    path('room-list/', login_required(views.room_list_view)),
]