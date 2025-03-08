"""UI for Lets Go Hike streamlit app"""

import streamlit as st
#import pandas as pd
#import folium
#from folium.plugins import MarkerCluster
#from streamlit_folium import st_folium
#from util.common_util import clean_float
#from util.weather_util import fetch_weather, get_weather_description
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
            .search-container {
            }
            /* Remove default padding around main block to make full-width usage easier */
            .main > div {
                padding-top: 1rem;
                padding-bottom: 0rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Let's Go Hike!</h1>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="search-container">', unsafe_allow_html=True)
        search_module = SearchModule("alltrails-data.csv")
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
    