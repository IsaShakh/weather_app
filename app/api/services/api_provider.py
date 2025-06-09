import requests
from datetime import datetime, timezone
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")  
TIMEOUT = 5

def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    data = resp.json()
    temp = data['main']['temp']
    offset = data['timezone']
    utc_now = datetime.now(timezone.utc)
    local_ts = utc_now.timestamp() + offset
    local_time = datetime.fromtimestamp(local_ts).strftime('%H:%M')
    return {'temperature': temp, 'local_time': local_time}


def get_real_forecast(city, date):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    
    try:
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    data = resp.json()
    target = date.strftime("%Y-%m-%d")
    temps = [entry['main']['temp'] for entry in data['list'] if entry['dt_txt'].startswith(target)]
    if not temps:
        return None
    return {'min_temperature': min(temps), 'max_temperature': max(temps)}

