from django.urls import path
from app.api.views import CurrentWeatherView, ForecastWeatherView


urlpatterns = [
    path('current', CurrentWeatherView.as_view()),
    path('forecast', ForecastWeatherView.as_view()),
]