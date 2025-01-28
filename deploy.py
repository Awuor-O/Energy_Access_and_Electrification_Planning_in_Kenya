import json
import pandas as pd
import gdown
import streamlit as st

# Download kmeans.csv
kmeans_url = 'https://drive.google.com/uc?export=download&id=16XSXBJGGxrbOtRNGc0e3oFijwo5UZN-m'
gdown.download(kmeans_url, 'kmeans.csv', quiet=False, fuzzy=True)

# Download kenya.geojson
geojson_url = 'https://drive.google.com/uc?export=download&id=1TwTR4N_hPOhynP6_vz45hN7qlSv_Le7a'
gdown.download(geojson_url, 'kenya.geojson', quiet=False, fuzzy=True)

# Load files
kmeans_df = pd.read_csv("kmeans.csv")
with open("kenya.geojson") as f:
    kenya_geojson = json.load(f)

# Separate data by cluster for easier plotting
cluster_0 = kmeans_df[kmeans_df['Cluster'] == 0]
cluster_1 = kmeans_df[kmeans_df['Cluster'] == 1]

import plotly.express as px

if isinstance(kenya_geojson, list):
    kenya_geojson = {"type": "FeatureCollection", "features": kenya_geojson}

# Kenya's map
fig = px.choropleth_mapbox(
    geojson=kenya_geojson,
    locations=kenya_geojson['features'],
    color_discrete_sequence=["#A9A9A9"],
    center={"lat": -1.286389, "lon": 36.817223},
    zoom=6,
    mapbox_style="carto-positron"
)

# Cluster 0 points = yellow markers
fig.add_scattermapbox(
    lat=cluster_0['Latitude'],
    lon=cluster_0['Longitude'],
    mode='markers',
    marker=dict(size=5, color='yellow'),
    name='Cluster 0: Suitable for Wind Farms and Microgrids'
)

# Cluster 1 points = blue markers
fig.add_scattermapbox(
    lat=cluster_1['Latitude'],
    lon=cluster_1['Longitude'],
    mode='markers',
    marker=dict(size=5, color='blue'),
    name='Cluster 1: More Developed Areas'
)

st.plotly_chart(fig)