from rest_framework import serializers
from datetime import datetime, timedelta
from app.models import Forecast

class ForecastSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=["%d.%m.%Y"])

    class Meta:
        model = Forecast
        fields = ("city", "date", "min_temperature", "max_temperature")
        validators = []

    def validate(self, data):
        today = datetime.today().date()

        if data["date"] < today:
            raise serializers.ValidationError("дата не может быть в прошлом")
        if data["date"] > today + timedelta(days=10):
            raise serializers.ValidationError("Прогноз можно задать максимум на 10 дней вперёд")
        if data["min_temperature"] > data["max_temperature"]:
            raise serializers.ValidationError("Минимальная температура не может быть больше максимальной")
        return data