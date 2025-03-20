"""Hike description for selected hike

Uses google genAI to generate hike descriptions
"""
import streamlit as st
import google.generativeai as genai


class HikeDescriptionModule:
    """
    Class for creating description of hike using google genAI LLM
    """
    def get_trek_description(self, trek_name, api_key):
        """
        Generates a trek description using Google Gemini API.

        """
        try:
            genai.configure(api_key=api_key)

            model = genai.GenerativeModel("gemini-2.0-flash")
            prompt = f"""Give me a detailed description of the trek in less than
                     150 words strictly {trek_name}. Include location, difficulty, duration, 
                     best season, and highlights. do not bold the output."""

            response =  model.generate_content(prompt)

            return response.text
        # pylint: disable=broad-exception-caught
        except Exception as e:
            return  f"Issues with genai: {str(e)}" #"Issues with genai"

    def display(self):
        """
        Displays hike description in streamlit app
        """
        selected_hike = st.session_state.get("selected_hike")
        #st.write("Selected Hike:", selected_hike)

        if selected_hike:
            trek_city = selected_hike.get('city_name')
            trek_name = selected_hike.get('name')
            formatted_trek = f"{trek_name}, {trek_city} "
            st.header(formatted_trek)
            # pylint: disable=invalid-name
            GEMINI_API_KEY = "AIzaSyD5d5iMJMXYQmOh3UqAj3zzHgle3MnMeEM"
            description = self.get_trek_description(trek_name, GEMINI_API_KEY)

            if description:
                st.write(description)
            else:
                st.write("No description available")
