# my_module.py

import streamlit as st
import pandas as pd

class HikeMapModule:
    def __init__(self):
        """
        You can store any needed state or initialization data here.
        For example, if your module needs to load a dataset, you could do it in the constructor.
        """
        self.data = pd.DataFrame({
            'lat': [37.773972],
            'lon': [-122.431297]
        })

    def display(self):
        """
        This method can be called in your main Streamlit app to render
        this module’s UI elements on the page.
        """
        st.header("Trail Map")
        st.map(self.data)

