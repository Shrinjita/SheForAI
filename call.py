import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Load India-specific GeoJSON with state boundaries
with open('india_states_boundaries.json') as f:
    india_states_geojson = json.load(f)

# Define data for states with unique colors
data = {
    'State_Name': ['Tamil Nadu', 'Telangana', 'Madhya Pradesh', 'Haryana', 'Chhattisgarh', 'Maharashtra',
                   'Tripura', 'Karnataka', 'Kerala', 'Uttar Pradesh', 'Assam', 
                   'West Bengal', 'Gujarat', 'Odisha', 'Rajasthan', 'Himachal Pradesh', 'Punjab', 'Bihar', 'Jharkhand'],
    'color': ["#FF5733", "#33FF57", "#3357FF", "#FFFF33", "#FF33FF", "#66FF66",
              "#FF3399", "#FF3366", "#33FF99", "#66CCFF", "#FF6600", "#FF66FF", 
              "#33CCFF", "#66FFCC", "#99FF33", "#339933", "#9933FF", "#CC33FF", "#33FFFF"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color mapping dictionary
state_color_map = dict(zip(df['State_Name'], df['color']))

# Plot India-only choropleth map with filled states
fig = px.choropleth_mapbox(
    df,
    geojson=india_states_geojson,
    featureidkey="properties.State_Name",
    locations="State_Name",
    color="State_Name",  # Use State_Name to apply the color mapping
    color_discrete_map=state_color_map,  # Use the predefined colors for each state
    hover_name="State_Name",
    title="India States Colored Map",
    mapbox_style="carto-positron",
    center={"lat": 20.5937, "lon": 78.9629},  # Center the map on India
    zoom=4  # Zoom level to focus on India
)

# Set figure size for better view
fig.update_layout(
    autosize=False,
    width=1000,
    height=700
)

# Display the map in Streamlit
st.title("India States Colored Map")
st.plotly_chart(fig)
