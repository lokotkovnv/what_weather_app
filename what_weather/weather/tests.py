from django.test import TestCase
from unittest.mock import patch
from .services import get_coordinates, get_weather
import requests


class ServicesTests(TestCase):

    @patch('weather.services.OCG.geocode')
    def test_get_coordinates_success(self, mock_geocode):
        mock_geocode.return_value = [
            {'geometry': {'lat': 55.7558, 'lng': 37.6173}}
        ]
        city = 'Москва'
        result = get_coordinates(city)
        self.assertIsNotNone(result)
        self.assertEqual(result, (55.7558, 37.6173))

    @patch('weather.services.OCG.geocode')
    def test_get_coordinates_failure(self, mock_geocode):
        mock_geocode.return_value = []
        city = 'НекорректныйГород'
        result = get_coordinates(city)
        self.assertIsNone(result)

    @patch('weather.services.requests.get')
    def test_get_weather_success(self, mock_get):
        mock_response = {
            'daily': {
                'time': ['2024-07-19', '2024-07-20'],
                'temperature_2m_max': [25.0, 26.0],
                'temperature_2m_min': [15.0, 16.0]
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        lat, lng = 55.7558, 37.6173
        result = get_weather(lat, lng)
        self.assertIsNotNone(result)
        self.assertEqual(result['daily']['time'], ['2024-07-19', '2024-07-20'])
        self.assertEqual(result['daily']['temperature_2m_max'], [25.0, 26.0])
        self.assertEqual(result['daily']['temperature_2m_min'], [15.0, 16.0])

    @patch('weather.services.requests.get')
    def test_get_weather_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException

        lat, lng = 55.7558, 37.6173
        result = get_weather(lat, lng)
        self.assertIsNone(result)
