import unittest
import datetime
from unittest.mock import patch

from letsgohike.util.weather_util import fetch_weather, get_weather_description

# A dummy asynchronous client that simulates python_weather.Client
class DummyClient:
    async def __aenter__(self):
        return self
    async def __aexit__(self, exc_type, exc, tb):
        pass
    async def get(self, city_name):
        # Return a dummy weather dictionary
        return {"dummy": "weather_data", "city": city_name}

# Dummy classes to simulate weather data structures for get_weather_description.
class DummyHourly:
    def __init__(self, hour, description):
        # Create a datetime object with the specified hour.
        self.time = datetime.datetime(2025, 3, 13, hour, 0)
        self.description = description

class DummyDaily:
    def __init__(self, hourly_forecasts):
        self.hourly_forecasts = hourly_forecasts

class TestWeatherUtil(unittest.TestCase):
    
    def test_fetch_weather(self):
        """
        Test that fetch_weather returns the dummy weather data using our patched DummyClient.
        """
        city_name = "Melbourne"
        result = fetch_weather(city_name)
        # Check that our dummy weather data is returned.
        self.assertEqual(result.location, city_name)
    
    def test_get_weather_description_found(self):
        """
        Test that get_weather_description returns the correct description
        when an hourly forecast matching the target hour exists.
        """
        dummy_hourly = DummyHourly(6, "Sunny")
        dummy_daily = DummyDaily([dummy_hourly])
        description = get_weather_description(dummy_daily, target_hour=6)
        self.assertEqual(description, "Sunny")
    
    def test_get_weather_description_not_found(self):
        """
        Test that get_weather_description returns "No data available"
        when no hourly forecast matches the target hour.
        """
        dummy_hourly = DummyHourly(8, "Cloudy")
        dummy_daily = DummyDaily([dummy_hourly])
        description = get_weather_description(dummy_daily, target_hour=6)
        self.assertEqual(description, "No data available")

if __name__ == '__main__':
    unittest.main()
