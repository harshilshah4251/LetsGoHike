import streamlit as st
import pandas as pd
import sqlite3
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Title of the app
st.title("Let's Go Hike")

# Sidebar for user input
st.sidebar.header("Filter Options")

# User input for filtering
difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Moderate", "Hard", "All"])
elevation = st.sidebar.slider("Select Elevation Gain (ft)", 0, 5000, (500, 3000))

# Display user selection
st.write(f"You selected difficulty: {difficulty} and elevation gain between {elevation[0]} and {elevation[1]} feet.")

# Load trail data from SQLite database
@st.cache_data
def load_data():
    # Connect to SQLite database
    conn = sqlite3.connect('trails_demo_data.db')  # Ensure the path is correct
    query = "SELECT * FROM trails_demo_data"  # Assuming your table is named 'trails_demo_data'
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Load the data
df = load_data()

# Filter the dataset based on user input
filtered_df = df.copy()

# Filter by difficulty
if difficulty != "All":
    filtered_df = filtered_df[filtered_df["Difficulty"] == difficulty]

# Filter by elevation gain
filtered_df = filtered_df[
    (filtered_df["Elevation_Gain"] >= elevation[0]) & (filtered_df["Elevation_Gain"] <= elevation[1])
]

# Display the filtered results
st.write("### Filtered Trail Results", filtered_df)

# Create a Folium map centered around a default location (you can change this)
m = folium.Map(location=[47.6, -122.3], zoom_start=20)

# Create a marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers for each trail in the filtered DataFrame
for _, row in filtered_df.iterrows():
    # Assuming your dataframe has 'Latitude' and 'Longitude' columns
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"Trail: {row['Name']}<br>Difficulty: {row['Difficulty']}<br>Elevation: {row['Elevation_Gain']} ft",
    ).add_to(marker_cluster)

# Display the map in Streamlit
st.write("### Trails on the Map")
folium_static(m)

