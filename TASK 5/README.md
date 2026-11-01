Project 05 – Weather App with Live OpenWeather API

Description

A Python-based weather application that retrieves real-time weather information and a five-day forecast using the OpenWeather API.

Features

- Display current temperature.
- Show weather description.
- Display humidity and wind speed.
- Retrieve a five-day weather forecast.
- Change the city.
- Handle invalid city names and API errors.

Technologies Used

- Python
- Requests
- OpenWeather API
- JSON
- Python-dotenv

Installation

Install the required libraries:

pip install requests python-dotenv

API Key Setup

Create a ".env" file in the project folder:

OPENWEATHER_KEY=YOUR_API_KEY

Replace "YOUR_API_KEY" with your own API key.

Security: Never upload your ".env" file or API key to GitHub.

How to Run

python weather_app.py

Testing

The application can be tested with different cities, including London and Mumbai. It also handles invalid city names and API errors.

Author

Python Project – InternCircle
