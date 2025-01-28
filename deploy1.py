import pandas as pd
import plotly.graph_objects as go
import gdown
import streamlit as st

# Download kmeans.csv
kmeans_url = 'https://drive.google.com/uc?export=download&id=16XSXBJGGxrbOtRNGc0e3oFijwo5UZN-m'
gdown.download(kmeans_url, 'kmeans.csv', quiet=False, fuzzy=True)

kmeans_df = pd.read_csv('kmeans.csv')

# Separate data by cluster
cluster_0 = kmeans_df[kmeans_df['Cluster'] == 0]
cluster_1 = kmeans_df[kmeans_df['Cluster'] == 1]

# Create the map
fig = go.Figure()

# Add scatter points for Cluster 0
fig.add_trace(
    go.Scattermapbox(
        lat=cluster_0['Latitude'],
        lon=cluster_0['Longitude'],
        mode='markers',
        marker=dict(size=5, color='yellow'),
        name='Cluster 0: Suitable for Wind Farms and Microgrids',
    )
)

# Add scatter points for Cluster 1
fig.add_trace(
    go.Scattermapbox(
        lat=cluster_1['Latitude'],
        lon=cluster_1['Longitude'],
        mode='markers',
        marker=dict(size=5, color='blue'),
        name='Cluster 1: More Developed Areas',
    )
)

# Set the layout for the map
fig.update_layout(
    mapbox=dict(
        style="carto-positron",
        center={"lat": -1.286389, "lon": 36.817223},  # Center on Kenya
        zoom=6,
    ),
    margin={"r":0, "t":0, "l":0, "b":0},  # No margins
)

# Render the map in Streamlit
st.plotly_chart(fig)
