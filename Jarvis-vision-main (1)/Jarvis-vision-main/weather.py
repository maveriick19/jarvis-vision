import requests
# from voice.text_to_speech import speak

def get_weather(city="Noida"):
    api_key = "use_your_api_key"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            temperature = main["temp"]
            weather_desc = data["weather"][0]["description"]
            return f"The current temperature in {city} is {temperature}°C with {weather_desc}."
        else:
            return "City not found."
    except Exception as e:
        return "Failed to get weather data."

# weather_info = get_weather("Noida")
# speak(weather_info)