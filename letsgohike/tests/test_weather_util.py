"""
Unit tests for the weather_util module.
"""

import unittest
import datetime
from unittest.mock import patch

# pylint: disable=import-error,no-name-in-module
from letsgohike.util.weather_util import fetch_weather, get_weather_description

# pylint: disable=too-few-public-methods
class DummyWeather:
    """Dummy weather object with a location attribute."""
    def __init__(self, city):
        self.location = city


class DummyClient:
    """
    A dummy asynchronous client simulating python_weather.Client.
    """
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass
    # pylint: disable=pointless-string-statement,missing-function-docstring
    async def get(self, city_name):
        # Return a DummyWeather object with the location set to city_name.
        return DummyWeather(city_name)

# pylint: disable=too-few-public-methods
class DummyHourly:
    """
    Dummy hourly forecast object to simulate the weather data structure.
    """
    def __init__(self, hour, description):
        # Create a datetime object with the specified hour.
        self.time = datetime.datetime(2025, 3, 13, hour, 0)
        self.description = description

# pylint: disable=too-few-public-methods
class DummyDaily:
    """
    Dummy daily forecast object containing hourly forecasts.
    """
    def __init__(self, hourly_forecasts):
        self.hourly_forecasts = hourly_forecasts


class TestWeatherUtil(unittest.TestCase):
    """
    Test cases for weather utility functions.
    """

    #@patch('letsgohike.util.weather_util.python_weather.Client', new=DummyClient)
    def test_fetch_weather(self):
        """
        Test that fetch_weather returns the dummy weather data using the patched DummyClient.
        """
        city_name = "Melbourne"
        result = fetch_weather(city_name)
        # Verify that the dummy weather object has the expected location.
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
