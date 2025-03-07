import python_weather
import asyncio

async def getWeather(city_name):
    """Fetch weather data for a city asynchronously."""
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city_name)
        return weather  # Return weather data instead of printing

def fetch_weather(city_name):
    """Helper function to run async function synchronously."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(getWeather(city_name))

def get_weather_description(daily, target_hour=6):
    """Extracts the closest hourly weather description for a given hour (default: 8 AM)."""
    for hourly in daily.hourly_forecasts:
        if hourly.time.hour == target_hour:
            return hourly.description  # Return weather description
    return "No data available"