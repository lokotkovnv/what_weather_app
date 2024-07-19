from typing import Dict, Tuple

import requests
from django.conf import settings
from opencage.geocoder import OpenCageGeocode

OCG = OpenCageGeocode(settings.OCG_API_KEY)


def get_coordinates(city: str) -> Tuple[float, float]:
    '''Получает координаты для заданного города'''
    try:
        result = OCG.geocode(city)
        if result:
            return result[0]['geometry']['lat'], result[0]['geometry']['lng']
        else:
            print(f'{settings.GEOCODER_ERROR_MSG_1} {city}')
            return None
    except Exception as e:
        print(f'{settings.GEOCODER_ERROR_MSG} {e}')
        return None


def get_weather(lat: float, lng: float) -> Dict:
    '''Получает данные прогноза погоды для заданных координат'''

    url = (
        f'{settings.WEATHER_API_URL}?latitude={lat}&longitude={lng}'
        '&daily=temperature_2m_max,temperature_2m_min'
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f'{settings.WEATHER_ERROR_MSG} {e}')
        return None
