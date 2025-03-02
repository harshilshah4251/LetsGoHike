"""Data management functions for the Lets Go Hike app """
import pandas as pd
import streamlit as st

def filter_hikes(df, difficulty, elevation):
    """filter hikes based on given user input"""
    filtered_df = df.copy()
    if difficulty != "All":
        filtered_df = filtered_df[filtered_df["Difficulty"] == difficulty]

    filtered_df = filtered_df[
        (filtered_df["elevation_gain"] >= elevation[0]) &
        (filtered_df["elevation_gain"] <= elevation[1])
    ]
    return filtered_df

@st.cache_data
def load_hike_data():
    """load hike attribute data and prep data"""
    df = pd.read_csv('alltrails-data.csv')
    return df
