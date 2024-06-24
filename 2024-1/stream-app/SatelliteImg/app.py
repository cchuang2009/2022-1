import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pystac_client import Client
from odc.stac import load


# Main Streamlit app starts here
st.write("Welcome to Satellite Visualization App by Streamlit...")

# Display Title
st.title("Satellite Map Portal")
st.markdown("Enter the data below.")

# Initialize session state for date_labels and user_date
if 'date_labels' not in st.session_state:
    st.session_state.date_labels = []

if 'data' not in st.session_state:
    st.session_state.data = None

if 'user_date' not in st.session_state:
    st.session_state.user_date = None

if 'user_date_index' not in st.session_state:
    st.session_state.user_date_index = 0

collections=["sentinel-2-l2a"]
columns = ['collection', 'start_date', 'end_date', 'min_cloud_cover', 'max_cloud_cover', 'longitude', 'latitude','buffer']



def search_satellite_images(collection="sentinel-2-l2a",
                            bbox=[-120.15,38.93,-119.88,39.25],
                            date="2023-06-01/2023-06-30",
                            cloud_cover=(0, 10)):
    
    # Define the search client
    client=Client.open("https://earth-search.aws.element84.com/v1")
    search = client.search(collections=[collection],
                            bbox=bbox,
                            datetime=date,
                            query=[f"eo:cloud_cover<{cloud_cover[1]}", f"eo:cloud_cover>{cloud_cover[0]}"])

    # Print the number of matched items
    print(f"Number of images found: {search.matched()}")

    data = load(search.items(), bbox=bbox, groupby="solar_day", chunks={})

    print(f"Number of days in data: {len(data.time)}")

    return data

def get_bbox_with_buffer(latitude=37.2502, longitude=-119.7513, buffer=0.01):
    
    min_lat = latitude - buffer
    max_lat = latitude + buffer
    min_lon = longitude - buffer
    max_lon = longitude + buffer
    
    bbox = [min_lon, min_lat, max_lon, max_lat]
    return bbox

# Create an empty DataFrame with these columns
df = pd.DataFrame(columns=columns)

if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(columns=df.columns)


# New Data
with st.form(key="test"):
    
    collection=st.selectbox("collection*",options=collections,index=None)
    start_date = st.date_input(label="start_date*")
    end_date = st.date_input(label="end_date*")
    max_cloud_cover  = st.number_input(label="max_cloud_cover*",value=10)
    longitude=st.number_input(label="longitude*", format="%.4f",value=-119.7513)
    latitude=st.number_input(label="latitude*", format="%.4f",value=37.2502)
    buffer=st.number_input(label="buffer (0.01 = 1 km)*", format="%.2f",value=0.01)

    # Mark Mandatory fields
    st.markdown("**required*")

    submit_button_run = st.form_submit_button(label="Run")
    submit_button_list = st.form_submit_button(label="List Available Images")
    submit_button_viz = st.form_submit_button(label="Visualize")

    if submit_button_run:
        new_df=pd.DataFrame(
            [
                {   
                    "collection": collection,
                    "start_date":start_date.strftime("%Y-%m-%d"),
                    "end_date": end_date.strftime("%Y-%m-%d"),
                    "max_cloud_cover":max_cloud_cover,
                    "longitude": longitude,
                    "latitude": latitude,
                    "buffer": buffer,

                }
            ]
        )
        
        st.session_state.mdf = pd.concat([st.session_state.mdf, new_df], axis=0)
        st.dataframe(st.session_state.mdf)
        st.success("Your request successfully submitted!")

        data = search_satellite_images(collection=collection,
                                       date=f"{start_date}/{end_date}",
                                       cloud_cover=(0, max_cloud_cover),
                                       bbox=get_bbox_with_buffer(latitude=latitude, longitude=longitude, buffer=buffer))
        st.session_state.data = data

        date_labels = []
        # Determine the number of time steps
        numb_days = len(data.time)
        # Iterate through each time step
        for t in range(numb_days):
            scl_image = data[["scl"]].isel(time=t).to_array()
            dt = pd.to_datetime(scl_image.time.values)
            year = dt.year
            month = dt.month
            day = dt.day
            date_string = f"{year}-{month:02d}-{day:02d}"
            date_labels.append(date_string)
        
        st.session_state.date_labels= date_labels
