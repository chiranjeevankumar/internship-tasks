import os
import requests
from dotenv import load_dotenv
from datetime import datetime
# Load API key from .env or environment variable
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"
def check_api_key():
    if not API_KEY:
        print("API key not found. Please configure OPENWEATHER_KEY.")
        return False
    return True
def handle_error(response):
    if response.status_code == 404:
        print("City not found. Please enter a valid city name.")
    elif response.status_code == 401:
        print("Invalid or inactive API key.")
    else:
        print("API error:", response.status_code)
def get_current_weather(city):
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            handle_error(response)
            return
        data = response.json()
        print("\n===== CURRENT WEATHER =====")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    except requests.RequestException as error:
        print("Connection error:", error)
def get_forecast(city):
    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            handle_error(response)
            return
        data = response.json()
        # Select one forecast near 12 PM for each day
        daily_forecasts = {}
        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]
            forecast_time = datetime.strptime(
                item["dt_txt"], "%Y-%m-%d %H:%M:%S"
            )
            if date not in daily_forecasts:
                daily_forecasts[date] = item
            else:
                existing_time = datetime.strptime(
                    daily_forecasts[date]["dt_txt"],
                    "%Y-%m-%d %H:%M:%S"
                )
                if abs(forecast_time.hour - 12) < abs(existing_time.hour - 12):
                    daily_forecasts[date] = item
        print("\n===== 5-DAY WEATHER FORECAST =====")
        print("City:", data["city"]["name"])
        for date, item in list(daily_forecasts.items())[:5]:
            print("\nDate:", date)
            print("Temperature:", item["main"]["temp"], "°C")
            print("Weather:", item["weather"][0]["description"])
            print("Humidity:", item["main"]["humidity"], "%")
            print("Wind Speed:", item["wind"]["speed"], "m/s")
    except requests.RequestException as error:
        print("Connection error:", error)
def weather_app():
    if not check_api_key():
        return
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return
    while True:
        print("\n========== WEATHER APP ==========")
        print("1. Current Weather")
        print("2. 5-Day Forecast")
        print("3. Change City")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            get_current_weather(city)
        elif choice == "2":
            get_forecast(city)
        elif choice == "3":
            new_city = input("Enter new city name: ").strip()
            if new_city:
                city = new_city
                print("City changed to:", city)
            else:
                print("City name cannot be empty.")
        elif choice == "4":
            print("Thank you for using Weather App!")
            break
        else:
            print("Invalid choice. Please select 1 to 4.")
# Run the application
weather_app()
