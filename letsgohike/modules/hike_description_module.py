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
import google.generativeai as genai




class HikeDescriptionModule:
    def get_trek_description(self, trek_name, api_key):
        """
        Generates a trek description using Google Gemini API.

        """
        try:
            genai.configure(api_key=api_key)

            model = genai.GenerativeModel("gemini-1.5-pro")
            prompt = f"Give me a detailed description of the trek in less than 150 words strictly {trek_name}. Include location, difficulty, duration, best season, and highlights."

            response =  model.generate_content(prompt)
        
            return response.text  
            
        except Exception as e:
            return  f"Issues with genai: {str(e)}" #"Issues with genai"  

    def display(self):
        selected_hike = st.session_state.get("selected_hike")
        #st.write("Selected Hike:", selected_hike)
        
        if selected_hike:
            trek_city = selected_hike.get('city_name')
            trek_name = selected_hike.get('name')
            formatted_trek = f"{trek_name},{trek_city} "
            #st.write("Selected Hike:", formatted_trek)
    
            #trek_name = "Mt. Rainier"
            st.write("Selected Hike:", formatted_trek)
            GEMINI_API_KEY = "AIzaSyD5d5iMJMXYQmOh3UqAj3zzHgle3MnMeEM"
            description = self.get_trek_description(trek_name, GEMINI_API_KEY)
            #description = "test1"

            if description:
                st.write(description)
            else:
                st.write("No description available")
