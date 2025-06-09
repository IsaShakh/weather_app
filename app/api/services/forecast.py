from app.models import Forecast
from .api_provider import get_real_forecast

def get_forecast_data(city, date):
    forecast = Forecast.objects.filter(city__iexact=city, date=date).first()
    if forecast:
        return {
            "min_temperature": forecast.min_temperature,
            "max_temperature": forecast.max_temperature
        }
    return get_real_forecast(city, date)

def save_or_update_forecast(validated_data):
    Forecast.objects.update_or_create(
        city=validated_data['city'],
        date=validated_data['date'],
        defaults={
            'min_temperature': validated_data['min_temperature'],
            'max_temperature': validated_data['max_temperature']
        }
    )
