

import streamlit as st
import requests

class HikePictureModule:
    def get_trek_image(self, trek_name, google_api_key, cse_id):
        """
        Fetches an image of the trek using Google Custom Search API.

        :param trek_name: Name of the trek
        :param google_api_key: Google API Key
        :param cse_id: Google Custom Search Engine (CSE) ID
        :return: URL of the first relevant image or an error message.
        """
        search_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "q": trek_name + " trek",
            "cx": cse_id,
            "key": google_api_key,
            "searchType": "image",
            "num": 1
        }
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}

        try:
            response = requests.get(search_url, params=params, headers=headers)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        except requests.exceptions.RequestException as e:
            return f"Error Occurred: {str(e)}"

        results = response.json()

        # Check if the API returned an error in its JSON response
        if "error" in results:
            error_info = results["error"]
            return f"Error Occurred: {error_info.get('message', 'Unknown error')}"

        # Check if the 'items' key exists and is not empty
        if "items" in results and results["items"]:
            return results["items"][0]["link"]
        else:
            return "No image found for this trek."

    def display(self):
        selected_hike = st.session_state.get("selected_hike")
        trek_city = selected_hike.get('city_name')
        trek_name = selected_hike.get('name')
        formatted_trek = f"{trek_name},{trek_city} "
        #st.write("Selected Hike:", formatted_trek)
        #st.write(selected_hike)
        if selected_hike:
            st.header("Hike Picture")
            #trek_name = selected_hike.get('city_name', 'Unknown Trek')
            trek_name = formatted_trek
            #st.write(trek_name)
            # --- API Keys and Search Engine ID ---
            
            GOOGLE_SEARCH_API_KEY = "AIzaSyDY9xD6sO6PZC5Cl_6YVlGavSQvmRJTJyo"
            GOOGLE_CSE_ID = "95b8f0ed307d1444b"

            # --- Fetch trek image ---
            image_url = self.get_trek_image(trek_name, GOOGLE_SEARCH_API_KEY, GOOGLE_CSE_ID)

            # If the returned URL is an error message, display it as text.
            if image_url.startswith("Error Occurred") or image_url.startswith("No image found"):
                st.write(image_url)
            else:
                # --- Display image in the Streamlit app ---
                st.markdown(
                    f'<a href="{image_url}" target="_blank"><img src="{image_url}" width="500"></a>',
                    unsafe_allow_html=True
                )

    def hike_list_image(self, hike_name):
        # --- API Keys and Search Engine ID ---
        GOOGLE_SEARCH_API_KEY = "AIzaSyDY9xD6sO6PZC5Cl_6YVlGavSQvmRJTJyo"
        GOOGLE_CSE_ID = "95b8f0ed307d1444b"

        image_url =  self.get_trek_image(hike_name, GOOGLE_SEARCH_API_KEY, GOOGLE_CSE_ID)

        # Use a placeholder image if an error occurred or no image is found
        if image_url.startswith("Error Occurred") or image_url.startswith("No image found"):
            image_url = self.get_trek_image(hike_name, GOOGLE_SEARCH_API_KEY, GOOGLE_CSE_ID)

        st.markdown(
            f"""
            <style>
                .cropped-image {{
                    width: 300px;  /* Set desired width */
                    height: 180px; /* Set desired height */
                    object-fit: cover; /* Crops image to fit without distortion */
                    border-radius: 10px; /* Optional: rounded corners */
                    display: block;
                    margin: auto;
                }}
            </style>
            <img src="{image_url}" class="cropped-image">
            """,
            unsafe_allow_html=True
        )
