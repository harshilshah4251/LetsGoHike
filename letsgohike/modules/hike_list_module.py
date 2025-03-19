"""
Module for displaying a list of hikes using Streamlit.
"""

import streamlit as st
import pandas as pd
from letsgohike.modules.hike_picture_module import HikePictureModule

# pylint: disable=too-few-public-methods
class HikeListModule:
    """
    A module to display a list of hikes with detailed information and a selection button.
    """

    def display(self):
        """
        Display the hike list with styling and details.
        
        Retrieves hikes from session state (or an empty DataFrame if none exist) and displays
        each hike in a styled layout with a "Select" button. When a hike is selected, it is
        stored in the session state.
        """
        hike_picture_module = HikePictureModule()

        # Render custom CSS for the hike container and title.
        st.markdown(
            """
            <style>
            .hike-container {
                background-color: #e0f0d8; /* Light greenish background */
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 15px;
                margin-bottom: 15px;
            }
            .hike-title {
                font-size: 10.0rem;
                font-weight: bold;
                margin: 5px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Retrieve hikes from session state or default to an empty DataFrame.
        hikes = st.session_state.get("search_hikes_output", pd.DataFrame())

        for index, hike in hikes.iterrows():
            st.markdown(f"<p class='hike-title'>{hike['name']}</p>", unsafe_allow_html=True)
            # Create two columns: left for the title and right for the select button.
            col_pic, col_left, col_right = st.columns([0.4, 0.4, 0.2])

            with col_pic:
                hike_picture_module.hike_list_image(hike['name'])

            with col_left:
                st.markdown(
                    f"""
                    <p><strong>Location:</strong> {hike['city_name']}, {hike['state_name']}</p>
                    <p><strong>Length:</strong> {hike['Distance_Miles']} miles</p>
                    <p><strong>Difficulty:</strong> {hike['Difficulty']}</p>
                    <p><strong>Rating:</strong> {hike['avg_rating']} ({hike['num_reviews']} reviews)</p>
                    <p><strong>Distance Away:</strong> {f"{hike['Distance away (miles)']:.1f}"} miles</p>   
                    """,
                    unsafe_allow_html=True
                )

            with col_right:
                # Render the "Select" button on the top-right.
                if st.button("Select", key=f"select_{index}"):
                    st.session_state.selected_hike = hike.to_dict()
                    # Optionally, you can call st.experimental_rerun() to refresh the page.

            st.markdown("<hr>", unsafe_allow_html=True)
            
