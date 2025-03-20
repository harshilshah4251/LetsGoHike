"""User search and filter hikes module for the Lets Go Hike app.

This module provides the SearchModule class, which allows users to search
and filter hikes based on location, difficulty, trail length, and elevation gain.
"""

import pandas as pd
import streamlit as st
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from letsgohike.util.hike_util import load_hike_data


class SearchModule:
    """Generates a navigation bar for searching and filtering hikes."""

    def __init__(self, csv_file):
        """Load hike data and initialize the geolocator.

        Args:
            csv_file: Path or file-like object to the CSV file containing hike data.
        """
        self.trails = load_hike_data(csv_file)
        self.geolocator = Nominatim(user_agent="hiking_app")

    def get_user_input(self):
        """Collect user input for location, difficulty, trail length, and elevation gain using a form.

        Returns:
            tuple or None: A tuple (location, difficulty, trail length range, elevation gain range)
            if the form is submitted, or None otherwise.
        """
        with st.form("search_form"):
            row1 = st.columns([2, 1, 1])
            location = row1[0].text_input("Enter a location (city, zip, etc.):")
            distance_away = row1[1].selectbox("Select distance away (miles):", [20, 50, 100], index = 1)
            difficulty = row1[2].selectbox("Select difficulty:", ["", "Easy", "Moderate", "Difficult"])

            row2 = st.columns([1, 1])
            user_length = row2[0].slider(
                "Trail length range (miles):",
                min_value=0.0,
                max_value=20.0,
                value=(0.0, 8.0)
            )
            user_elevation = row2[1].slider(
                "Elevation gain range (ft):",
                min_value=0,
                max_value=14050,
                value=(0, 1500)
            )

            row3 = st.columns([1, 1, 14])
            submitted = row3[0].form_submit_button("Search")
            reset = row3[1].form_submit_button("Reset")

        if reset:
            return "", "", (0.0, 10.0), (0, 2000), 50

        if submitted:
            return location, difficulty.lower(), user_length, user_elevation, distance_away

        return None

    # pylint: disable=too-many-arguments, too-many-positional-arguments
    def find_nearest_trails(self, location, difficulty, length_range, elevation_range,
                            max_distance_away=100):
        """Find the closest hiking trails based on user input.

        Args:
            location (str): The location input by the user.
            difficulty (str): The difficulty level (e.g., 'easy', 'moderate', 'difficult').
            length_range (tuple): A tuple (min, max) representing the trail length range in miles.
            elevation_range (tuple): A tuple (min, max) representing the elevation gain range in feet.
            max_distance_away (int, optional): Maximum allowable distance (in miles) from the user location.
                                               Defaults to 100.

        Returns:
            pd.DataFrame: A DataFrame containing the filtered trails, or an empty DataFrame if no trails match.
        """
        if not location:
            st.warning("Please enter a location.")
            return pd.DataFrame()

        try:
            # Get user location's latitude and longitude.
            user_location = self.geolocator.geocode(location)
            if not user_location:
                st.error("Location not found. Try a different location.")
                return pd.DataFrame()

            user_coords = (user_location.latitude, user_location.longitude)

            # Compute distances from the user location.
            self.trails["Distance away (miles)"] = self.trails.apply(
                lambda row: geodesic(user_coords, (row["Latitude"], row["Longitude"])).miles,
                axis=1
            )

            filtered_trails = self.trails[
                ((self.trails["Difficulty"].str.lower() == difficulty) if difficulty else True) &
                (self.trails["Distance_Miles"].between(length_range[0], length_range[1])) &
                (self.trails["elevation_gain"].between(elevation_range[0], elevation_range[1])) &
                (self.trails["Distance away (miles)"] <= max_distance_away)
            ].sort_values(by="Distance away (miles)")

            st.session_state.search_hikes_output = filtered_trails
            return filtered_trails
        # pylint: disable=broad-exception-caught
        except Exception as e:
            # Optionally log or display the error: st.error(f"Error finding trails: {e}")
            return pd.DataFrame()

    def display(self):
        """Display the search form and filter results on the UI."""
        user_input = self.get_user_input()
        if user_input is None:
            return

        location, difficulty, length, elevation, max_distance = user_input
        results = self.find_nearest_trails(location, difficulty, length, elevation, max_distance)
        if results is not None and not results.empty:
            st.success(f"Found {len(results)} matching trails!")
            return results
        else:
            st.info("No matching trails found.")
