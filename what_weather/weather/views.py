import datetime as dt

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import CityForm
from .models import SearchHistory
from .services import get_coordinates, get_weather


def city_form(request):
    '''Обрабатывает форму ввода города'''
    last_city = request.session.get('last_city', '')

    if 'city' in request.GET:
        city = request.GET['city']
        coordinates = get_coordinates(city)
        if coordinates:
            lat, lng = coordinates
            request.session['last_city'] = city
            if request.user.is_authenticated:
                SearchHistory.objects.create(user=request.user, city=city)
            return weather_forecast(request, city, lat, lng)
        else:
            error_message = f'{settings.CITY_NOT_FOUND_MSG} {city}.'
            form = CityForm()
            context = {
                'form': form,
                'error_message': error_message,
                'last_city': last_city
            }
            return render(request, 'weather/city_form.html', context)

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            coordinates = get_coordinates(city)
            if coordinates:
                lat, lng = coordinates
                request.session['last_city'] = city
                if request.user.is_authenticated:
                    SearchHistory.objects.create(user=request.user, city=city)
                return weather_forecast(request, city, lat, lng)
            else:
                error_message = f'{settings.CITY_NOT_FOUND_MSG} {city}.'
        else:
            error_message = settings.FORM_ERROR_MSG
        context = {
            'form': form,
            'error_message': error_message,
            'last_city': last_city
        }
        return render(request, 'weather/city_form.html', context)
    else:
        form = CityForm(initial={'city': last_city})
    return render(
        request, 'weather/city_form.html',
        {'form': form, 'last_city': last_city}
    )


def weather_forecast(request, city: str, lat: float, lng: float):
    '''Отображает прогноз погоды'''
    weather_data = get_weather(lat, lng)
    if weather_data and 'daily' in weather_data:
        dates = weather_data['daily']['time']
        max_temps = weather_data['daily']['temperature_2m_max']
        min_temps = weather_data['daily']['temperature_2m_min']

        forecast = []
        for date, max_temp, min_temp in zip(dates, max_temps, min_temps):
            formatted_date = dt.datetime.strptime(
                date, '%Y-%m-%d').strftime('%d.%m.%Y')
            forecast.append({
                'date': formatted_date,
                'max_temp': max_temp,
                'min_temp': min_temp
            })

        context = {
            'city': city,
            'forecast': forecast,
        }
        return render(request, 'weather/weather_forecast.html', context)
    else:
        error_message = settings.WEATHER_NOT_FOUND_MSG
        context = {'error_message': error_message}
        return render(request, 'weather/city_form.html', context)


def reset_session(request):
    request.session.flush()
    return redirect('weather:city_form')


def register(request):
    '''Регистрация пользователей'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('weather:city_form')
    else:
        form = UserCreationForm()
    return render(request, 'weather/register.html', {'form': form})
