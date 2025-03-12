# my_module.py

import streamlit as st

from letsgohike.util.weather_util import fetch_weather


class WeatherModule:
    def __init__(self):
        pass
    def display(self):
        st.header("Current Weather")

        # Fetch weather data using python-weather
        if st.session_state.get("selected_hike") is not None:
            city = st.session_state.get("selected_hike")['city_name'] 
            st.header("3‑Day Weather Forecast")
            st.write(f"Forecast for **{city}**")

            # Fetch weather data using your utility.
            weather_data = fetch_weather(city)
            if not weather_data:
                st.write("Could not fetch weather data.")
                return

            # Use daily_forecasts if available; otherwise, use forecasts.
            daily_forecasts = weather_data.daily_forecasts

            if not daily_forecasts:
                st.write("No daily forecast data available.")
                return

            # Define target hours (in 24-hour format)
            target_hours = [6, 9, 12, 15, 18]

            # For each day in the forecast...
            for daily in daily_forecasts:
                # Format the date for display.
                date_str = daily.date.strftime("%A, %B %d")
                with st.expander(f"📅 **{date_str}**"):
                    html_table = "<table style='width:100%; text-align:center; border-collapse: collapse;'><tr>"
                    for target_hour in target_hours:
                        # Find the hourly forecast matching the target hour.
                        hourly = None
                        for h in daily.hourly_forecasts:
                            if h.time.hour == target_hour:
                                hourly = h
                                break

                        if hourly:
                            # Map parts of the description to an appropriate icon.
                            desc_lower = hourly.description.lower()
                            weather_icons = {
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
                            icon_url = None
                            for key, url in weather_icons.items():
                                if key in desc_lower:
                                    icon_url = url
                                    break
                            if icon_url is None:
                                icon_url = "https://openweathermap.org/img/wn/01d@2x.png"

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