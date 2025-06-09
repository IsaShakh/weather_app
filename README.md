# Weather Forecast API

Проект реализует REST API для получения текущей и прогнозной погоды, а также ручного переопределения прогноза на определённую дату.



## Используемый источник данных

Для получения реальных погодных данных используется публичный API от OpenWeather:

- https://openweathermap.org/api

Методы:
- **Current Weather**: `https://api.openweathermap.org/data/2.5/weather`
- **Forecast**: `https://api.openweathermap.org/data/2.5/forecast`


## Основной функционал

- `GET /api/weather/current?city=...` — получить текущую погоду для города.
- `GET /api/weather/forecast?city=...&date=...` — получить прогноз на указанную дату (реальный или переопределённый).
- `POST /api/weather/forecast` — вручную задать прогноз на дату (сохранение в БД).


## Дополнительная информация

- Используемые технологии: **Django**, **Django REST Framework**, **PostgreSQL**, **python-decouple**.
- Конфигурация API-ключа и БД вынесена в `.env` файл.
- Переопределённые прогнозы хранятся в базе и имеют приоритет над данными OpenWeather.




