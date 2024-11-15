import pandas as pd
import folium
import geopandas as gpd

# Load crime data
df = pd.read_csv('/mnt/c/Users/Shrinjita Paul/Documents/GitHub/SheForAI/CrimesOnWomenData.csv')
geojson_file = '/mnt/c/Users/Shrinjita Paul/Documents/GitHub/SheForAI/india_state_geo.json'

gdf = gpd.read_file(geojson_file)

# Aggregate data by state and crime type
state_crime_data = df.groupby('State').sum().reset_index()

# Initialize base map
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Define crime types and color schemes
crime_types = {
    'Rape': 'YlOrRd',
    'K&A': 'Blues',
    'DD': 'Purples',
    'AoW': 'Oranges',
    'AoM': 'Greens',
    'DV': 'Reds',
    'WT': 'PuRd'
}

# Add choropleth layers for each crime type
for crime, color in crime_types.items():
    # Merge GeoDataFrame with state crime data
    gdf_crime = gdf.merge(state_crime_data[['State', crime]], left_on='NAME_1', right_on='State', how='left')

    # Create choropleth layer
    folium.Choropleth(
        geo_data=gdf_crime,
        name=f"{crime} Incidents",
        data=state_crime_data,
        columns=['State', crime],
        key_on="feature.properties.NAME_1", 
        fill_color=color,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=f"{crime} Incidents by State"
    ).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Display map
m.save('/mnt/c/Users/Shrinjita Paul/Documents/GitHub/SheForAI/crimes_against_women_map.html')  # Save the map to an HTML file
