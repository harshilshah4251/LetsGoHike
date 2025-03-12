"""Data management functions for the Lets Go Hike app """
import pandas as pd
import streamlit as st

@st.cache_data
def load_hike_data(trails_csv):
    """load hike attribute data and prep data"""
    if trails_csv:
        df = pd.read_csv(trails_csv)
        df['Lat'] = df['Lat'].str.replace('"', '', regex=True)
        df['Lat'] = df['Lat'].str.replace(',', '', regex=True)
        df['Lat'] = df['Lat'].str.replace(' ', '', regex=True)
        df['Lat'] = df['Lat'].str.replace("'", '', regex=True)
        df['Lat'] = df['Lat'].str.replace("|", '', regex=True)
        df['Lat'] = df['Lat'].str.replace("l", '', regex=True)
        df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
        df['Latitude'] = df['Lat']
        df['Longitude'] = df['Long']
        return df
    else:
        return None
