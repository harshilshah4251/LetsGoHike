# my_module.py

import streamlit as st
import pandas as pd

class HikeListModule:
    def __init__(self):
        pass

    def display(self):
        # print("in display")
        st.header("Hike List")

        # Optional: Light green background for each hike box.
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
                font-size: 1.2rem;
                font-weight: bold;
                margin: 0;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if st.session_state.get("search_hikes_output") is not None:
            hikes = st.session_state.get("search_hikes_output")
        else:
            hikes = pd.DataFrame()

        for index, hike in hikes.iterrows():

            # Start the styled container
            
            # Create a row with two columns: left for the title, right for the select button
            col_left, col_right = st.columns([0.8, 0.2])

            with col_left:
                # Display hike name in a styled paragraph
                st.markdown(f"<p class='hike-title'>{hike['name']}</p>", unsafe_allow_html=True)
            with col_right:
                pass
                # Render the "Select" button on the top-right
                if st.button("Select", key=f"select_{index}"):
                    st.session_state.selected_hike = hike.to_dict()
                    # st.rerun()
            
            # Display other key details below the top row
            st.markdown(
                f"""
                <p><strong>Location:</strong> {hike['city_name']}, {hike['state_name']}</p>
                <p><strong>Length:</strong> {hike['length']} {hike['units']}</p>
                <p><strong>Difficulty:</strong> {hike['Difficulty']}</p>
                <p><strong>Rating:</strong> {hike['avg_rating']} ({hike['num_reviews']} reviews)</p>
                <p><strong>Distance Away:</strong> {hike['Distance away (miles)']} miles</p>
                """,
                unsafe_allow_html=True
            )
            st.markdown("<hr>", unsafe_allow_html=True)
