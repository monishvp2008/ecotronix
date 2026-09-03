# Proprietary License
# Copyright (c) 2025 Monish. All rights reserved.
# Unauthorized copying, distribution, or modification is prohibited.
import requests
def sanitize_city(city: str) -> str:
    # Remove any non-alphabetic characters except spaces
    return ''.join(c for c in city if c.isalpha() or c.isspace()).strip()
def get_detailed_weather(city: str, api_key: str) -> str:
    city = sanitize_city(city)
    if not city:
        return "Invalid city name. Please provide a valid city."
    if not api_key or not isinstance(api_key, str):
        return "Weather API key is missing or invalid."
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'weather' in data and 'main' in data and 'wind' in data:
                weather = data['weather'][0]['description']
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                # Scientific agricultural advice based on weather
                advice = []
                if temp > 35:
                    advice.append("High temperature detected. Consider irrigation and shade for crops.")
                elif temp < 15:
                    advice.append("Low temperature detected. Protect sensitive crops from cold stress.")
                if humidity < 30:
                    advice.append("Low humidity. Monitor for drought stress and irrigate as needed.")
                elif humidity > 80:
                    advice.append("High humidity. Watch for fungal diseases in crops.")
                if 'rain' in weather.lower():
                    advice.append("Rain expected. Avoid pesticide application and plan for drainage.")
                if wind_speed > 10:
                    advice.append("Strong winds detected. Secure young plants and greenhouse structures.")

                advice_text = "\n- " + "\n- ".join(advice) if advice else "No specific advice for current conditions."

                return (
                    f"Weather in {city.title()}:\n"
                    f"- Condition: {weather}\n"
                    f"- Temperature: {temp}°C\n"
                    f"- Humidity: {humidity}%\n"
                    f"- Wind Speed: {wind_speed} m/s\n"
                    f"Agricultural Advice:{advice_text}"
                )
            else:
                return f"Weather data for {city.title()} is incomplete. Please try another city or check spelling."
        elif response.status_code == 404:
            return f"City '{city.title()}' not found. Please check the city name and try again."
        elif response.status_code == 401:
            return "Invalid API key for weather service. Please check your API key."
        else:
            return "Unable to fetch weather data. Please try again later."
    except requests.exceptions.Timeout:
        return "Weather service timed out. Please try again later."
    except Exception:
        return "An unexpected error occurred while fetching weather data. Please try again later."