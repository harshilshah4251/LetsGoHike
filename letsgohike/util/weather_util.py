"""
Module for fetching and processing weather data asynchronously using python_weather.
"""

import asyncio
import python_weather


async def get_weather(city_name):
    """Fetch weather data for a city asynchronously.

    Args:
        city_name (str): The name of the city to fetch weather for.

    Returns:
        Weather: An object containing the weather data.
    """
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city_name)
        return weather  # Return weather data instead of printing


def fetch_weather(city_name):
    """Run the asynchronous get_weather function synchronously.

    Args:
        city_name (str): The name of the city to fetch weather for.

    Returns:
        Weather: An object containing the weather data.
    """
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        weather = loop.run_until_complete(get_weather(city_name))
    finally:
        loop.close()
    return weather


def get_weather_description(daily, target_hour=6):
    """Extract the weather description for a specific target hour from daily forecasts.

    Args:
        daily: An object with an attribute 'hourly_forecasts' containing forecast data.
        target_hour (int, optional): The target hour (in 24-hour format) to extract the description.
                                     Defaults to 6.

    Returns:
        str: The weather description if available; otherwise, "No data available".
    """
    for hourly in daily.hourly_forecasts:
        if hourly.time.hour == target_hour:
            return hourly.description  # Return weather description
    return "No data available"
