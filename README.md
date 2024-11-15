# SheForAI


Data Loading:

The pandas library is used to load a CSV file containing crime data on women (CrimesOnWomenData.csv), which includes crime statistics by state.
A GeoJSON file (india_state_geo.json) is used, which contains the geographical shapes of the states of India.
Data Processing:

The crime data is aggregated by state using groupby('State') to sum the crime counts for each state.
A GeoDataFrame (gdf) is loaded from the GeoJSON file to provide the geographical boundaries of each state.
Map Initialization:

A base map centered on India is created using folium.Map() with a starting zoom level of 5.
Crime Type and Color Scheme:

A dictionary (crime_types) maps each type of crime (e.g., Rape, Kidnapping & Abduction) to a color scheme for the choropleth layer.
Choropleth Layer Creation:

For each crime type, the corresponding data from state_crime_data is merged with the geographical data (gdf), and a choropleth layer is created for each crime type using folium.Choropleth().
The map shows the intensity of each crime type with different color schemes representing the count of crimes in each state.
Layer Control:

A folium.LayerControl() is added to allow users to toggle between different crime type layers on the map.
Saving the Map:

The final map is saved as an HTML file (crimes_against_women_map.html), which can be viewed in a browser.
Usage:
To use this code, ensure that the CSV file and GeoJSON file are correctly formatted and accessible in the specified paths (/content/CrimesOnWomenData.csv and /content/india_state_geo.json).
Once the map is generated, you can open the HTML file in any browser to view the interactive map, displaying crimes against women by state.
Potential Enhancements:
Additional Crime Data: Incorporate more crime data or other types of gender-related crimes.
Time-based Analysis: Allow users to filter the data based on time (e.g., year-wise analysis).
Interactive Features: Add pop-ups or tooltips to show more detailed information about each state when clicked.
This map can be a powerful tool for policymakers, researchers, and social activists to identify regions with high crime rates and plan interventions accordingly.
