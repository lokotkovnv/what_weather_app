from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from weather.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='weather/login.html', success_url='/'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
