"""UI for Let's Go Hike Streamlit app.

This module defines the main user interface for the Lets Go Hike application,
assembling various modules such as search, hike description, picture, map, and weather.
"""

import streamlit as st
import pandas as pd
# pylint: disable=import-error,no-name-in-module
from letsgohike.modules.hike_description_module import HikeDescriptionModule
# pylint: disable=import-error,no-name-in-module
from letsgohike.modules.hike_list_module import HikeListModule
# pylint: disable=import-error,no-name-in-module
from letsgohike.modules.hike_map_module import HikeMapModule
# pylint: disable=import-error,no-name-in-module
from letsgohike.modules.hike_picture_module import HikePictureModule
# pylint: disable=import-error,no-name-in-module
from letsgohike.modules.search_module import SearchModule
# pylint: disable=import-error,no-name-in-module
from letsgohike.modules.weather_module import WeatherModule
# pylint: disable=import-error,no-name-in-module
from letsgohike.modules.hike_plan_module import HikePlanModule # type: ignore

st.set_page_config(page_title="Let's Go Hike!", page_icon="🏞️", layout="wide")


def main():
    """Main UI structure for the Let's Go Hike Streamlit app."""
    # Initialize modules.
    hike_description_module = HikeDescriptionModule()
    hike_picture_module = HikePictureModule()
    hike_map_module = HikeMapModule()
    weather_module = WeatherModule()
    hike_plan_module= HikePlanModule()

    # Apply custom CSS styles.
    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 1rem;
            }
            .main > div {
                padding-top: 1rem;
                padding-bottom: 0rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>Let's Go Hike!</h1>", unsafe_allow_html=True)

    # Display the search module in its own container.
    with st.container():
        st.markdown('<div class="search-container">', unsafe_allow_html=True)
        # Re-instantiate search_module if needed.
        search_module = SearchModule("alltrails-data.csv")
        search_module.display()
        st.markdown('</div>', unsafe_allow_html=True)

    # Create two equal columns for displaying the hike list and additional modules.
    col_left, col_right = st.columns([1, 1])

    with col_left:
        # Hike list module.
        hike_list_module = HikeListModule()
        if not "search_hikes_output" in st.session_state:
            st.info("🔍 Use the search bar above to find hikes.")
        else:
            hike_list_module.display()

    with col_right:
        if not "selected_hike" in st.session_state:
            st.warning("👈 Select a hike from the list to see details here.")
        else:
            # Row 1: Hike description and hike picture.
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
            row3_col1, row3_col2 = st.columns(2)
            with row3_col2:
                hike_plan_module.display()


if __name__ == "__main__":
    main()
