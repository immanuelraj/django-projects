from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_view
from users import views
from users.forms import UserLoginForm


urlpatterns = [
    path('hotel/', include('hotel.urls', namespace='hotel')),
    path('activity', include('activity.urls', namespace='activity')),
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/login/', auth_view.LoginView.as_view(), name='login'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name="login.html",authentication_form=UserLoginForm),name='login'),
    path('accounts/logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]