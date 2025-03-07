# my_module.py

import streamlit as st

class HikeDescriptionModule:
    def __init__(self):
        """
        You can store any needed state or initialization data here.
        For example, if your module needs to load a dataset, you could do it in the constructor.
        """
        self.title = "Mountain Adventure"
        self.description = (
            "Experience an unforgettable hike through challenging terrain with breathtaking vistas "
            "at every turn. Perfect for those seeking a mix of adventure and nature."
        )
        self.details = "Distance: 8 miles | Difficulty: Moderate | Duration: 4 hours"

    def display(self):
        """
        This method can be called in your main Streamlit app to render
        this module’s UI elements on the page.
        """
        st.header(self.title)
        st.write(self.description)
        st.write(self.details)
