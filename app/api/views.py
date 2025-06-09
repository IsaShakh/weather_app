from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta

from .serializers import ForecastSerializer
from .services.api_provider import get_current_weather
from .services.forecast import get_forecast_data, save_or_update_forecast

class CurrentWeatherView(APIView):
    def get(self, request):
        city = request.query_params.get("city")
        if not city:
            return Response({"error": "Параметр city обязателен"}, status=400)

        data = get_current_weather(city)
        if not data:
            return Response({"error": "Город не найден"}, status=404)

        return Response(data)


class ForecastWeatherView(APIView):
    def get(self, request):
        city = request.query_params.get("city")
        date_str = request.query_params.get("date")

        if not city or not date_str:
            return Response({"error": "Нужны параметры city и date"}, status=400)

        try:
            date = datetime.strptime(date_str, "%d.%m.%Y").date()
        except ValueError:
            return Response({"error": "Неверный формат даты. Используйте dd.MM.yyyy"}, status=400)

        today = datetime.today().date()
        if date < today:
            return Response({"error": "Дата не может быть в прошлом"}, status=400)
        if date > today + timedelta(days=10):
            return Response({"error": "Можно только на 10 дней вперёд"}, status=400)

        data = get_forecast_data(city, date)
        if not data:
            return Response({"error": "Нет данных или город не найден"}, status=404)

        return Response(data)

    def post(self, request):
        serializer = ForecastSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        save_or_update_forecast(serializer.validated_data)
        return Response(serializer.data, status=201)
