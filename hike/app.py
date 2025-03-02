"""UI for Lets Go Hike streamlit app"""

import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import hike_data_manager

st.title("Let's Go Hike")

#filter sidebar
st.sidebar.header("Filter Options")
if "filter_difficulty" not in st.session_state:
    st.session_state["filter_difficulty"] = "All"
if "filter_elevation" not in st.session_state:
    st.session_state["filter_elevation"] = (500, 3000)
if "apply_filters" not in st.session_state:
    st.session_state["apply_filters"] = False

difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Moderate", "Hard", "All"],
                                  index=["Easy", "Moderate", "Hard", "All"].index(
                                  st.session_state["filter_difficulty"]))
elevation = st.sidebar.slider("Select Elevation Gain (ft)", 0, 5000,
                                st.session_state["filter_elevation"])

# Search Button
if st.sidebar.button("🔍 Search for Hikes"):
    st.session_state["filter_difficulty"] = difficulty
    st.session_state["filter_elevation"] = elevation
    st.session_state["apply_filters"] = True
    st.rerun()

# Only apply filters when the button is clicked
if st.session_state["apply_filters"]:
    df = hike_data_manager.load_hike_data()
    filtered_df = hike_data_manager.filter_hikes(df, st.session_state["filter_difficulty"],
                                        st.session_state["filter_elevation"])
else:
    filtered_df = pd.DataFrame()

# Initialize saved hikes list in session state if not already present
if "saved_hikes" not in st.session_state:
    st.session_state["saved_hikes"] = []

# Display saved hikes in sidebar
st.sidebar.subheader("Saved Hikes")
for i, hike in enumerate(st.session_state["saved_hikes"]):
    col1, col2 = st.sidebar.columns([4, 1])  # Create columns for checkbox and remove button
    with col1:
        st.checkbox(hike["name"], key=f"saved_{i}")  # Checkbox for selection
    with col2:
        if st.button("❌", key=f"remove_{hike['name']}_{i}"):
            st.session_state["saved_hikes"].pop(i)
            st.rerun()

tab1, tab2, tab3 = st.tabs(["Explore Hikes", "Compare Hikes", "Training Plan"])

with tab1:
    hike_map, hike_desc = tab1.columns([3, 1])

    with hike_map.container():
        with st.container(height = 300):
            for _, row in filtered_df.iterrows():
                if st.button(row["name"], key=f"hike_button_{row['name']}"):
                    st.session_state["selected_hike"] = row
                    st.session_state["hike_selected"] = True
                    st.rerun()
        m = folium.Map(location=[47.6, -122.3], zoom_start=20)
        marker_cluster = MarkerCluster().add_to(m)
        for _, row in filtered_df.iterrows():
            folium.Marker(
                location=[float(row["Lat"]), float(row["Long"])],
                popup=f"Trail: {row['name']}<br>Difficulty: {row['Difficulty']}\
                        <br>Elevation: {row['elevation_gain']} ft",
            ).add_to(marker_cluster)
        st.write("### Trails on the Map")
        st_folium(m, width="100%", height=300)

    with hike_desc.container():
        st.subheader("Selected Hike")

        if st.session_state.get("hike_selected", True):
            hike = st.session_state["selected_hike"]
            st.subheader(hike["name"])
            st.write(f"**Difficulty:** {hike['Difficulty']}")

            if st.button("➕ Add Hike to List", key="add_hike"):
                if hike not in st.session_state["saved_hikes"]:
                    st.session_state["saved_hikes"].append(hike)
                    st.rerun()
        else:
            st.write("➡️ **Select a hike from the list or map to see details!**")

with tab2:
    st.header("Compare Hikes")
with tab3:
    st.header("Training plan")
