
import streamlit as st
import google.generativeai as genai




class HikePlanModule:
    def get_trek_plan(self, trek_name, api_key):
        """
        Generates a trek description using Google Gemini API.

        """
        try:
            genai.configure(api_key=api_key)

            model = genai.GenerativeModel("gemini-2.0-flash")
            prompt = (
                f"For {trek_name}, give a very brief, no more than 150 words to the point trek plan for an average trek enthusiast. "
                "It must include the following - any required gears, any vehicle permits or any special attribute that is specific to this location "
                "that must be considered. Start the result directly with bullets."
            )
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
            st.write(formatted_trek)
            
            GEMINI_API_KEY = "AIzaSyD5d5iMJMXYQmOh3UqAj3zzHgle3MnMeEM"
            description = self.get_trek_plan(trek_name, GEMINI_API_KEY)
            #description = "test1"

            if description:
                st.write(description)
            else:
                st.write("No description available")
