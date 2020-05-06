from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path("hotel/", include("hotel.urls", namespace="hotel")),
    path("activity/", include("activity.urls", namespace="activity")),
    path('admin/', admin.site.urls),
]