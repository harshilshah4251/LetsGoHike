# my_module.py

import streamlit as st

class HikeListModule:
    def __init__(self):
        """
        You can store any needed state or initialization data here.
        For example, if your module needs to load a dataset, you could do it in the constructor.
        """
        self.hikes = [
            {
                "title": "Mountain Trail",
                "difficulty": "Hard",
                "length": "12 miles",
                "elevation_gain": "1500 ft",
                "description": "A challenging hike through rugged terrain."
            },
            {
                "title": "Forest Walk",
                "difficulty": "Easy",
                "length": "3 miles",
                "elevation_gain": "200 ft",
                "description": "A relaxing stroll amidst towering trees."
            },
            {
                "title": "Coastal Path",
                "difficulty": "Medium",
                "length": "5 miles",
                "elevation_gain": "500 ft",
                "description": "Enjoy breathtaking ocean views on this moderate hike."
            },
            {
                "title": "Desert Run",
                "difficulty": "Hard",
                "length": "8 miles",
                "elevation_gain": "800 ft",
                "description": "Experience the vast and serene desert landscapes."
            }
        ]

    def display(self):
        """
        This method can be called in your main Streamlit app to render
        this module’s UI elements on the page.
        """
        st.header("Hike List Module")
        st.markdown(
            """
            <style>
            .hike-box {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                margin-bottom: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Iterate over each hike and display its details in a box.
        for hike in self.hikes:
            st.markdown(
                f"""
                <div class="hike-box">
                    <h3>{hike['title']}</h3>
                    <p><strong>Difficulty:</strong> {hike['difficulty']}</p>
                    <p><strong>Length:</strong> {hike['length']}</p>
                    <p><strong>Elevation Gain:</strong> {hike['elevation_gain']}</p>
                    <p>{hike['description']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
