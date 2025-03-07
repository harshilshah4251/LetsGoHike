# my_module.py

import streamlit as st

class HikePictureModule:
    def __init__(self):
        """
        You can store any needed state or initialization data here.
        For example, if your module needs to load a dataset, you could do it in the constructor.
        """
        self.image_url = "https://www.google.com/imgres?q=mount%20rainier&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Ff%2Ff9%2FRainier20200906.jpg%2F1200px-Rainier20200906.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMount_Rainier&docid=XifueVyfNKfZZM&tbnid=4kEUGz2Qb76ldM&w=1200&h=800&hcb=2"
        self.caption = "A beautiful view from the trail."

    def display(self):
        """
        This method can be called in your main Streamlit app to render
        this module’s UI elements on the page.
        """
        st.header("Hike Image")
        st.image(self.image_url, caption=self.caption)
