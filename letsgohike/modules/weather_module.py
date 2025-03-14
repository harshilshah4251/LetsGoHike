"""
Module for displaying weather information using Streamlit.
"""

import streamlit as st
# pylint: disable=import-error,no-name-in-module
from letsgohike.util.weather_util import fetch_weather

# Constant for weather icons mapping.
WEATHER_ICONS = {
    "clear": "https://openweathermap.org/img/wn/01d@2x.png",
    "partly cloudy": "https://openweathermap.org/img/wn/02d@2x.png",
    "cloudy": "https://openweathermap.org/img/wn/03d@2x.png",
    "overcast": "https://openweathermap.org/img/wn/04d@2x.png",
    "shower": "https://openweathermap.org/img/wn/09d@2x.png",
    "rain": "https://openweathermap.org/img/wn/10d@2x.png",
    "thunderstorm": "https://openweathermap.org/img/wn/11d@2x.png",
    "snow": "https://openweathermap.org/img/wn/13d@2x.png",
    "mist": "https://openweathermap.org/img/wn/50d@2x.png"
}

# pylint: disable=too-few-public-methods
class WeatherModule:
    """
    A module to display the current weather and a 3-day forecast
    for a selected hike using Streamlit.
    """

    def display(self):
        """
        Display the weather information.
        
        Uses the session state to determine the selected hike and then
        fetches and displays the weather forecast for the associated city.
        """
        st.header("Current Weather")

        selected_hike = st.session_state.get("selected_hike")
        if selected_hike:
            city = selected_hike.get("city_name")
            st.header("3‑Day Weather Forecast")
            st.write(f"Forecast for **{city}**")

            # Fetch weather data using the weather utility.
            weather_data = fetch_weather(city)
            if not weather_data:
                st.write("Could not fetch weather data.")
                return

            daily_forecasts = weather_data.daily_forecasts
            if not daily_forecasts:
                st.write("No daily forecast data available.")
                return

            # Define target hours (in 24-hour format).
            target_hours = [6, 9, 12, 15, 18]

            # Loop through each day in the forecast.
            for daily in daily_forecasts:
                date_str = daily.date.strftime("%A, %B %d")
                with st.expander(f"📅 **{date_str}**"):
                    html_table = (
                        "<table style='width:100%; text-align:center; border-collapse: collapse;'>"
                        "<tr>"
                    )
                    for target_hour in target_hours:
                        # Find the hourly forecast matching the target hour.
                        hourly = next(
                            (h for h in daily.hourly_forecasts if h.time.hour == target_hour),
                            None,
                        )
                        if hourly:
                            desc_lower = hourly.description.lower()
                            icon_url = next(
                                (url for key, url in WEATHER_ICONS.items() if key in desc_lower),
                                "https://openweathermap.org/img/wn/01d@2x.png",
                            )
                            cell = (
                                f"<td style='padding: 10px; border: 1px solid #ccc;'>"
                                f"<strong>{target_hour}:00</strong><br>"
                                f"<img src='{icon_url}' width='50'><br>"
                                f"{hourly.temperature}°F"
                                f"</td>"
                            )
                        else:
                            cell = (
                                f"<td style='padding: 10px; border: 1px solid #ccc;'>"
                                f"<strong>{target_hour}:00</strong><br>No data"
                                f"</td>"
                            )
                        html_table += cell
                    html_table += "</tr></table>"
                    st.markdown(html_table, unsafe_allow_html=True)
