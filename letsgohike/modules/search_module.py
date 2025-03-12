"""Let's go hike! user search and filter hikes"""
import pandas as pd
import streamlit as st
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from letsgohike.util.hike_util import load_hike_data

class SearchModule:
    """Generates navigation bar for searching and filtering hikes"""
    def __init__(self, csv_file):
        """load data and initialize geolocator"""
        st.session_state.all_data = load_hike_data(csv_file) 
        self.geolocator = Nominatim(user_agent="hiking_app")

    def get_user_input(self):
        """Collect user input for location, difficulty, and trail length using a form."""
        with st.form("search_form"):
            row1 = st.columns([3,1])
            location = row1[0].text_input("Enter a location (city, zip, etc.):")
            difficulty = row1[1].selectbox("Select difficulty:", ["Easy", "Moderate", "Difficult"])

            row2 = st.columns([1,1])
            user_length = row2[0].slider("Trail length range (miles):", min_value=0.0,
                                         max_value=20.0, value=(0.0,8.0))
            user_elevation = row2[1].slider("Elevation gain range (ft):", min_value=0,
                                            max_value=14050, value=(0, 1500))

            row3 = st.columns([1,1,14])
            submitted = row3[0].form_submit_button("Search")
            reset = row3[1].form_submit_button("Reset")

        if reset:
            return "", "Easy", (0.0, 10.0), (0, 2000)

        return location, difficulty.lower(), user_length, user_elevation if submitted else None

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
    def find_nearest_trails(self, location, difficulty, length_range, elevation_range,
                            max_distance_away=100):
        """Find the closest hiking trails based on user input."""
        if not location:
            st.warning("Please enter a location.")
            return pd.DataFrame()

        try:
            # Get user location's latitude and longitude
            user_location = self.geolocator.geocode(location)
            if not user_location:
                st.error("Location not found. Try a different location.")
                return pd.DataFrame()

            user_coords = (user_location.latitude, user_location.longitude)

            # Compute distances
            st.session_state.all_data["Distance away (miles)"] = st.session_state.all_data.apply(
                lambda row: geodesic(user_coords, (row["Latitude"], row["Longitude"])).miles, axis=1
            )

            filtered_trails =st.session_state.all_data[
                (st.session_state.all_data["Difficulty"].str.lower() == difficulty) &
                (st.session_state.all_data["Distance_Miles"].between(length_range[0], length_range[1])) &
                (st.session_state.all_data["elevation_gain"].between(elevation_range[0], elevation_range[1])) &
                (st.session_state.all_data["Distance away (miles)"] <= max_distance_away)
            ].sort_values(by="Distance away (miles)")
            st.session_state.search_hikes_output = filtered_trails
            return filtered_trails
        # pylint: disable=broad-exception-caught
        except Exception as e:
            # st.error(f"Error finding trails: {e}")
            return pd.DataFrame()

    def display(self):
        """"displays search and filter functions on UI"""
        location, difficulty, length, elevation = self.get_user_input()
        if location:
            results = self.find_nearest_trails(location, difficulty, length, elevation)

            if results is not None and not results.empty:
                st.success(f"Found {len(results)} matching trails!")
                return results
            else:
                print("No matching trails found.")
