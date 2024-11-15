# SheForAI - Women Safety App

The app also features a "Future Advancement Map," which highlights areas with safety scores based on different factors. The future version of this app will include a search bar and other features to further improve user experience.

## Project Overview

This app leverages geospatial data and heatmaps to visualize the safety situation in different areas. It uses the `femaleunsafe.json` file to zoom in on specific areas and calculate a safety score, providing a clear picture of the safety levels in various regions. The app is built with a simple user interface (UI) for ease of use and is intended to provide real-time help for women.

### Current Features:
- **Future Advancement Map**: Displays specific areas with safety scores based on the `femaleunsafe.json` file.
  - **Columns in `femaleunsafe.json`**:
    - `state`: Name of the state
    - `area`: Name of the area
    - `latitude`: Latitude of the location
    - `longitude`: Longitude of the location
    - `safety_score`: Safety score for the area
  
- **Basic UI**: Simple user interface to locate safe havens, police stations, and other safety resources nearby.
  
- **Heatmap Visualization**: Uses the `heatmap.py` script to generate a heatmap that visualizes the safety score data for specific regions.

- **Map Interface**: An interactive map (`map.html`) displaying the locations with safety scores and details about safe havens.

### Future Enhancements:
- **Search Bar**: To search for nearby safe havens, police stations, and other resources.
- **Improved Features**: More features to help users find real-time safety information in their area.

## Project Structure

- **`femaleunsafe.json`**: A JSON file containing location-based safety data. This file is used for the future advancement map.
- **`heatmap.py`**: A Python script used to generate a heatmap based on the safety score data from `femaleunsafe.json`.
- **`map.html`**: The HTML file containing the map that users can interact with to view the safety scores and location data.
- **`SheForAI`**: Main directory containing all the resources and scripts for the app.

## Installation

To run the app locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Shrinjita/SheForAI
   cd SheForAI
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the `heatmap.py` script to generate the heatmap:
   ```bash
   python heatmap.py
   ```

4. Open the generated `map.html` file in your browser to view the map and interact with the data.

## Technologies Used
- **Python**: For data processing and heatmap generation.
- **Folium**: For creating interactive maps.
- **GeoPandas**: For working with geospatial data.
- **JSON**: For storing the location-based safety data.

## Contribution

Shrinjita Paul
Ancy B John
Harshita Das
Monami Sen
