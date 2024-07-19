# What_weather

## Описание

Это веб-приложение для получения прогноза погоды, разработанное с использованием Django. Пользователь может ввести название города, чтобы получить прогноз погоды в этом городе на ближайшее время. Также реализована функция сохранения истории поисков и отображения частоты запросов по городам.

## Используемые технологии

- **Django**: Фреймворк для веб-разработки на Python, используемый для создания серверной части приложения.
- **Open-Meteo API**: API для получения данных о прогнозе погоды.
- **OpenCage Geocoding API**: API для получения координат по названию города.
- **Django REST Framework**: Для создания REST API, который возвращает частоту запросов по городам.
- **unittest**: Для написания тестов и проверки функциональности приложения.
## Установка и запуск

### 1. Клонирование репозитория

git clone git@github.com:lokotkovnv/what_weather_app.git

cd what_weather_app
### 2. Создание и активация виртуального окружения
Для Unix/Linux/MacOS:

python3 -m venv venv

source venv/bin/activate

Для Windows:

python -m venv venv

source venv\Scripts\activate
### 3. Установка зависимостей
pip install -r requirements.txt
### 4. Миграции базы данных
python manage.py migrate
### 5. Запуск сервера разработки
python manage.py runserver
### 6. Запуск тестов
Для запуска тестов используйте команду:
python manage.py test

### Автор
Локотков Никита

https://github.com/lokotkovnv
