# my_module.py

# import streamlit as st

# class HikeDescriptionModule:
#     def __init__(self):
#         """
#         You can store any needed state or initialization data here.
#         For example, if your module needs to load a dataset, you could do it in the constructor.
#         """
#         self.title = "Mountain Adventure"
#         self.description = (
#             "Experience an unforgettable hike through challenging terrain with breathtaking vistas "
#             "at every turn. Perfect for those seeking a mix of adventure and nature."
#         )
#         self.details = "Distance: 8 miles | Difficulty: Moderate | Duration: 4 hours"

#     def display(self):
#         """
#         This method can be called in your main Streamlit app to render
#         this module’s UI elements on the page.
#         """
#         st.header(self.title)
#         st.write(self.description)
#         st.write(self.details)




import streamlit as st
import genai


class HikeDescriptionModule:
    def get_trek_description(self, trek_name, api_key):
        """
        Generates a trek description using Google Gemini API.

        :param trek_name: Name of the trek
        :param api_key: Google Gemini API Key
        :return: Description of the trek
        """
        try:
            genai.configure(api_key=api_key)

            model = genai.GenerativeModel("gemini-1.5-pro")
            prompt = f"Give me a detailed description of the trek in less than 200 words {trek_name}. Include location, difficulty, duration, best season, and highlights."

            response = model.generate_content(prompt)
            return response.text  
        except:
            return "Issues with genai"  

    def display(self):
        st.header("Hike Description")
        selected_hike = st.session_state.get("selected_hike")
        if selected_hike:
            trek_name = selected_hike.get('city_name')
            GEMINI_API_KEY = "AIzaSyD5d5iMJMXYQmOh3UqAj3zzHgle3MnMeEM"
            description = self.get_trek_description(trek_name, GEMINI_API_KEY)
            if description:
                st.write(description)
            else:
                st.write("No description available")
