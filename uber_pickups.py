import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups NYC")

@st.cache
def load_data(nrows):
    data = pd.read_csv('uber-raw-data-sep14.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['date/time'] = pd.to_datetime(data['date/time'])
    return data

data_load_state = st.text("Data Loading")
data = load_data(1000)
data_load_state.text("data loading done")

if st.sidebar.checkbox("Show Raw Data"):
    st.write(data)

st.subheader("Number of pickups by hour")
hist_values = np.histogram(data['date/time'].dt.hour, bins = 24, range = (0,24))[0]
st.bar_chart(hist_values)

st.subheader("line Chart representation")
st.line_chart(hist_values)

st.subheader("map of all pickups")
st.map(data)

hour_to_filter= st.sidebar.slider('hour to check', 0, 23, 17)
filtered_data = data[data['date/time'].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

