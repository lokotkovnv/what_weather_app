from django.urls import path

from . import api_views, views

app_name = 'weather'

urlpatterns = [
    path('', views.city_form, name='city_form'),
    path('reset_session/', views.reset_session, name='reset_session'),
    path(
        'api/city_search_frequency/',
        api_views.city_search_frequency, name='city_search_frequency'
    ),
]
