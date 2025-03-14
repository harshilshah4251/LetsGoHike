import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

class HikeMapModule:
    def __init__(self):
        pass

    def display(self):
        st.header("Trail Map")

        # Check if a trail has been selected
        if "selected_hike" in st.session_state:
            selected_hike = st.session_state.selected_hike
            lat = selected_hike["Latitude"]  # Latitude from the selected trail
            lon = selected_hike["Longitude"]  # Longitude from the selected trail

            # Show the map of the selected trail's location
            st.write(f"Showing the trailhead for **{selected_hike['name']}** on the map...")

            # Create a folium map centered at the selected trail's location
            trail_map = folium.Map(location=[lat, lon], zoom_start=12)

            # Add a marker (pin) at the selected trailhead's location
            folium.Marker(
                location=[lat, lon],
                popup=f"<strong>{selected_hike['name']}</strong><br>{selected_hike['city_name']}, {selected_hike['state_name']}",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(trail_map)

            # Adjust the map to make sure the marker is visible within the viewport
            # Set the bounds of the map to a small area around the trailhead
            trail_map.fit_bounds([[lat - 0.05, lon - 0.05], [lat + 0.05, lon + 0.05]])

            # Display the map in the Streamlit app using st_folium
            st_folium(trail_map, width=700, height=400)

        else:
            st.warning("Please select a trail from the list to view its location on the map.")
