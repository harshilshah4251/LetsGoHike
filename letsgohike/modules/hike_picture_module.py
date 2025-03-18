# my_module.py

# import streamlit as st

# class HikePictureModule:
#     def __init__(self):
#         """
#         You can store any needed state or initialization data here.
#         For example, if your module needs to load a dataset, you could do it in the constructor.
#         """
#         self.image_url = "https://www.google.com/imgres?q=mount%20rainier&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Ff%2Ff9%2FRainier20200906.jpg%2F1200px-Rainier20200906.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMount_Rainier&docid=XifueVyfNKfZZM&tbnid=4kEUGz2Qb76ldM&w=1200&h=800&hcb=2"
#         self.caption = "A beautiful view from the trail."

#     def display(self):
#         """
#         This method can be called in your main Streamlit app to render
#         this module’s UI elements on the page.
#         """
#         st.header("Hike Image")
#         st.image(self.image_url, caption=self.caption)


import streamlit as st
import requests


class HikePictureModule:
    def get_trek_image(self, trek_name, google_api_key, cse_id):
        """
        Fetches an image of the trek using Google Custom Search API.

        :param trek_name: Name of the trek
        :param google_api_key: Google API Key
        :param cse_id: Google Custom Search Engine (CSE) ID
        :return: URL of the first relevant image
        """
        search_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "q": trek_name + " trek",
            "cx": cse_id,
            "key": google_api_key,
            "searchType": "image",
            "num": 1
        }

        response = requests.get(search_url, params=params)
        results = response.json()

        if "items" in results:
            return results["items"][0]["link"]
        else:
            return "No image found."

    def display(self):
        st.header("Hike Image")
        selected_hike = st.session_state.get("selected_hike")
        if selected_hike:
            trek_name = selected_hike.get('city_name')

            # --- API Keys and Search Engine ID ---
            GEMINI_API_KEY = "AIzaSyD5d5iMJMXYQmOh3UqAj3zzHgle3MnMeEM"
            GOOGLE_SEARCH_API_KEY = "AIzaSyA9bfi1p9yY7jmSZZsMLb6O0BttyYFan-o"
            GOOGLE_CSE_ID = "95b8f0ed307d1444b"

            # --- Fetch trek image ---
            image_url = self.get_trek_image(trek_name, GOOGLE_SEARCH_API_KEY, GOOGLE_CSE_ID)
            st.write("**Trek Image URL:**")
            st.write(image_url)

            # --- Display image in the Streamlit app ---
            st.image(image_url, caption=trek_name)
