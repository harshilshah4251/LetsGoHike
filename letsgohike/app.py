"""UI for Lets Go Hike streamlit app"""

import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from letsgohike.modules.hike_description_module import HikeDescriptionModule
from letsgohike.modules.hike_list_module import HikeListModule
from letsgohike.modules.hike_map_module import HikeMapModule
from letsgohike.modules.hike_picture_module import HikePictureModule
from letsgohike.modules.search_module import SearchModule
from letsgohike.modules.weather_module import WeatherModule
from letsgohike.util.hike_util import filter_hikes, load_hike_data
from util.common_util import clean_float
from util.weather_util import fetch_weather, get_weather_description

def main():
    search_module = SearchModule()
    hike_description_module = HikeDescriptionModule()
    hike_list_module = HikeListModule()
    hike_picture_module = HikePictureModule()
    hike_map_module = HikeMapModule()
    weather_module = WeatherModule()
    
    st.set_page_config(layout="wide")

    st.markdown("""
        <style>
            .block-container {
            }
            .search-container {
            }
            /* Remove default padding around main block to make full-width usage easier */
            .main > div {
                padding-top: 1rem;
                padding-bottom: 0rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.header("Lets Go Hike!")

    with st.container():
        st.markdown('<div class="search-container">', unsafe_allow_html=True)
        # Call your search module UI function here
        search_module = SearchModule()
        search_module.display()
        st.markdown('</div>', unsafe_allow_html=True)
    col_left, col_right = st.columns([1, 1])  # Adjust ratio as needed

    with col_left:
        # Hike list module
        hike_list_module.display()

    with col_right:
        # Create two rows, each with two columns
        # Row 1
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            hike_description_module.display()
        with row1_col2:
            hike_picture_module.display()

        # Row 2
        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            weather_module.display()
        with row2_col2:
            hike_map_module.display()
if __name__ == "__main__":
    main()




# #filter sidebar
# st.sidebar.header("Filter Options")
# if "filter_difficulty" not in st.session_state:
#     st.session_state["filter_difficulty"] = "All"
# if "filter_elevation" not in st.session_state:
#     st.session_state["filter_elevation"] = (500, 3000)
# if "apply_filters" not in st.session_state:
#     st.session_state["apply_filters"] = False

# difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Moderate", "Hard", "All"],
#                                   index=["Easy", "Moderate", "Hard", "All"].index(
#                                   st.session_state["filter_difficulty"]))
# elevation = st.sidebar.slider("Select Elevation Gain (ft)", 0, 5000,
#                                 st.session_state["filter_elevation"])

# # Search Button
# if st.sidebar.button("🔍 Search for Hikes"):
#     st.session_state["filter_difficulty"] = difficulty
#     st.session_state["filter_elevation"] = elevation
#     st.session_state["apply_filters"] = True
#     st.rerun()

# # Only apply filters when the button is clicked
# if st.session_state["apply_filters"]:
#     df = load_hike_data()
#     filtered_df = filter_hikes(df, st.session_state["filter_difficulty"],
#                                         st.session_state["filter_elevation"])
# else:
#     filtered_df = pd.DataFrame()

# # Initialize saved hikes list in session state if not already present
# if "saved_hikes" not in st.session_state:
#     st.session_state["saved_hikes"] = []

# # Display saved hikes in sidebar
# st.sidebar.subheader("Saved Hikes")
# for i, hike in enumerate(st.session_state["saved_hikes"]):
#     col1, col2 = st.sidebar.columns([4, 1])  # Create columns for checkbox and remove button
#     with col1:
#         st.checkbox(hike["name"], key=f"saved_{i}")  # Checkbox for selection
#     with col2:
#         if st.button("❌", key=f"remove_{hike['name']}_{i}"):
#             st.session_state["saved_hikes"].pop(i)
#             st.rerun()

# tab1, tab2, tab3 = st.tabs(["Explore Hikes", "Compare Hikes", "Training Plan"])

# with tab1:
#     hike_map, hike_desc = tab1.columns([3, 2])

#     with hike_map.container():
#         with st.container(height = 300):
#             for _, row in filtered_df.iterrows():
#                 if st.button(row["name"], key=f"hike_button_{row['trail_id']}"):
#                     st.session_state["selected_hike"] = row
#                     st.session_state["hike_selected"] = True
#                     st.rerun()
#         m = folium.Map(location=[47.6, -122.3], zoom_start=20)
#         marker_cluster = MarkerCluster().add_to(m)
#         for _, row in filtered_df.iterrows():
#             lat = clean_float(row["Lat"])
#             long = clean_float(row["Long"])
#             folium.Marker(
#                 location=[lat, long],
#                 popup=f"Trail: {row['name']}<br>Difficulty: {row['Difficulty']}\
#                         <br>Elevation: {row['elevation_gain']} ft",
#             ).add_to(marker_cluster)
#         st.write("### Trails on the Map")
#         st_folium(m, width="100%", height=300)

#     with hike_desc.container():
#         st.subheader("Selected Hike")

#         if st.session_state.get("hike_selected", True):
#             hike = st.session_state.get("selected_hike", None)
#             if hike is not None:
#                 st.subheader(hike["name"])
#                 st.write(f"**Difficulty:** {hike['Difficulty']}")

#                 # Extract city name for weather lookup
#                 city_name = hike["city_name"]
#                 state_name = hike["state_name"]

#                 st.write(f"📍 **Location:** {city_name}, {state_name}")

#                 weather_data = fetch_weather(city_name)
#                 if weather_data:
#                     st.write(f"🌡 Current Temperature: **{weather_data.temperature}°F**")

#                     st.subheader("📅 3-Day Weather Forecast")

#                     for daily in weather_data:
#                         date = daily.date.strftime("%A, %B %d")

#                         with st.expander(f"📅 **{date}**"):
#                             st.write(f"6 AM Weather: **{get_weather_description(daily, 6)}**")
#                             st.write(f"9 AM Weather: **{get_weather_description(daily, 9)}**")
#                             st.write(f"12 PM Weather: **{get_weather_description(daily, 12)}**")
#                             st.write(f"3 PM Weather: **{get_weather_description(daily, 15)}**")
#                             st.write(f"6 PM Weather: **{get_weather_description(daily, 18)}**")

#                 else:
#                     st.write("⚠️ Could not fetch weather data.")


#                 if st.button("➕ Add Hike to List", key="add_hike"):
#                     if hike not in st.session_state["saved_hikes"]:
#                         st.session_state["saved_hikes"].append(hike)
#                     st.rerun()

                
#             else:
#                 st.write("➡️ **Select a hike from the list or map to see details!**")

# with tab2:
#     st.header("Compare Hikes")
# with tab3:
#     st.header("Training plan")
