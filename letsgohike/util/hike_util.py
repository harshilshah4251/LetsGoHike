"""
Data management functions for the Lets Go Hike app.
"""

import pandas as pd
import streamlit as st


@st.cache_data
def load_hike_data(trails_csv):
    """Load hike attribute data from a CSV file and prepare the data.

    This function reads the CSV file containing hike data, cleans the 'Lat'
    column by removing unwanted characters, converts it to numeric, and
    assigns it to the 'Latitude' column. The 'Longitude' column is set using
    the 'Long' column from the CSV.

    Args:
        trails_csv: A CSV file or file-like object containing the hike data.

    Returns:
        pd.DataFrame: The processed DataFrame containing hike data,
                      or None if no CSV file is provided.
    """
    if trails_csv:
        df = pd.read_csv(trails_csv)
        # Remove unwanted characters from the 'Lat' column using a single regex.
        # Characters removed: double quotes ("), commas, spaces, single quotes ('),
        # vertical bars (|), and lowercase 'l'
        df['Lat'] = df['Lat'].str.replace(r'["\', |l]', '', regex=True)
        df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
        df['Latitude'] = df['Lat']
        df['Longitude'] = df['Long']
        return df
    return None
