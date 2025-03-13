"""UI for Lets Go Hike streamlit app"""

import streamlit as st
from letsgohike.modules.hike_description_module import HikeDescriptionModule
from letsgohike.modules.hike_list_module import HikeListModule
from letsgohike.modules.hike_map_module import HikeMapModule
from letsgohike.modules.hike_picture_module import HikePictureModule
from letsgohike.modules.search_module import SearchModule
from letsgohike.modules.weather_module import WeatherModule

st.set_page_config(page_title="Let's Go Hike!", page_icon="🏞️", layout="wide")

def main():
    """UI structure for Let's Go Hike streamlit app"""
    search_module = SearchModule("alltrails-data.csv")
    hike_description_module = HikeDescriptionModule()
    hike_list_module = HikeListModule()
    hike_picture_module = HikePictureModule()
    hike_map_module = HikeMapModule()
    weather_module = WeatherModule()

    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
            }
            .main > div {
                padding-top: 1rem;
                padding-bottom: 0rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Let's Go Hike!</h1>", unsafe_allow_html=True)

    # Search bar
    with st.container():
        search_module.display()

    # Main layout
    col_left, col_right = st.columns([1, 1])  # Adjust ratio if needed

    with col_left:
        # Hike list module
        hike_list_module.display()

    with col_right:
        # Trail description and picture side by side
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            hike_description_module.display()
        with row1_col2:
            hike_picture_module.display()

        # Row 2 with weather and map
        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            weather_module.display()  # Restored weather module here
        with row2_col2:
            hike_map_module.display()

if __name__ == "__main__":
    main()
