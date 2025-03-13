# my_module.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

class HikeMapModule:
    def __init__(self):
        """Initialize with an empty DataFrame"""
        self.data = pd.DataFrame(columns=["Latitude", "Longitude", "Trail Name"])

    def update_data(self, filtered_trails):
        """Update the map data with filtered results"""
        if filtered_trails is not None and not filtered_trails.empty:
            self.data = filtered_trails[["Latitude", "Longitude", "Trail Name"]]
        else:
            self.data = pd.DataFrame(columns=["Latitude", "Longitude", "Trail Name"])

    def display(self):
        """Display the map with filtered trail locations"""
        st.header("Trail Map")

        if self.data.empty:
            st.warning("No trails found for the selected filters. Try adjusting the search criteria.")
            return

        # Create a folium map centered on the first result
        center = [self.data.iloc[0]["Latitude"], self.data.iloc[0]["Longitude"]]
        hike_map = folium.Map(location=center, zoom_start=10)

        # Add markers for each trailhead
        for _, row in self.data.iterrows():
            folium.Marker(
                location=[row["Latitude"], row["Longitude"]],
                popup=row["Trail Name"],
                icon=folium.Icon(color="green", icon="cloud"),
            ).add_to(hike_map)

        # Render the folium map in Streamlit
        st_folium(hike_map, width=700, height=500)
